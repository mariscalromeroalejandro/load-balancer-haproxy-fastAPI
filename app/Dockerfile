FROM python:3.11-slim

WORKDIR /app

COPY app.py .

RUN pip install fastapi uvicorn

ENV INSTANCE_ID=1

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
