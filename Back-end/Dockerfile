FROM python:3.12-slim

WORKDIR /code

COPY . /code

RUN pip install -r requirements.txt

ENV PYTHONPATH=/code
EXPOSE 8000

CMD ["sh", "-c", "sleep 10 && python app/test/create_tables.py && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
