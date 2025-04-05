FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE ${FLASK_RUN_PORT}

CMD ["flask", "run", "--host=${FLASK_RUN_HOST}", "--port=${FLASK_RUN_PORT}"]