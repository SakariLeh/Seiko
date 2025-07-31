FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 4200

CMD ["sh", "-c", "gunicorn -w 4 -b $FLASK_RUN_HOST:$FLASK_RUN_PORT ${FLASK_APP%.py}:app"]
