FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8001

CMD ["sh", "-c", "sleep 10 && python main.py"]
