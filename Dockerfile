FROM hovanvydut/base-phobert
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--reload"]