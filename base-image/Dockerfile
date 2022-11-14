FROM huggingface/transformers-pytorch-cpu
WORKDIR /app

# Run main.py to pre-download model and save it in the image
COPY main.py .
RUN python3 main.py