FROM python:3.8-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:8000", "main:app"]