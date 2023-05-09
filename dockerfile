# syntax=docker/dockerfile:1

FROM python:3.11.3-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH='/'
COPY ./app /app
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

EXPOSE 5000

RUN pip install -r requirements.txt

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]