FROM python:3.10-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY ../requirements.txt .

RUN pip install --upgrade pip && pip install -r requrements.txt --no-cache-dir

COPY . .

ENV PATHOPATH '/app'