# web
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
app = FastAPI()

# ai
import torch
from transformers import RobertaForSequenceClassification, AutoTokenizer
model = RobertaForSequenceClassification.from_pretrained("wonrax/phobert-base-vietnamese-sentiment")
tokenizer = AutoTokenizer.from_pretrained("wonrax/phobert-base-vietnamese-sentiment", use_fast=False)


class ReqAnalyse(BaseModel):
    content: str

class Status(Enum):
    NEG = "NEG"
    POS = "POS"
    NEU = "NEU"

@app.post("/analyse-comment")
async def analyse_comment(req: ReqAnalyse):
    input_ids = torch.tensor([tokenizer.encode(req.content)])

    res = {
        "status": False,
        "confident": {
            "neg": 0,
            "pos": 0,
            "neu": 0
        }
    }
    with torch.no_grad():
        out = model(input_ids)
        result = out.logits.softmax(dim=-1).tolist()

        neg_confident = result[0][0]
        pos_confident = result[0][1]
        neu_confident = result[0][2]
        res["confident"] = {
            "neg": neg_confident,
            "pos": pos_confident,
            "neu": neu_confident
        }

        if (neg_confident > 0.5):
            res["status"] = Status.NEG.value
        if (pos_confident > 0.5):
            res["status"] = Status.POS.value
        if (neu_confident > 0.5):
            res["status"] = Status.NEU.value
    
    return res