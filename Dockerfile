FROM python:3.7-slim

WORKDIR /app-test-neuro

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . /app-test-neuro

CMD ["python3", "main.py"]