FROM python:3.8

RUN useradd -ms /bin/bash appuser
USER appuser
WORKDIR /usr/app/src
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
