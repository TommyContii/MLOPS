FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY scoring.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]