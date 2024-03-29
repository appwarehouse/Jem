
FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . ./app
EXPOSE 8000