FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
COPY main.py .
COPY app/ app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8001

CMD ["sh", "-c", "sleep 10 && python main.py"]
