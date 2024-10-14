FROM python:latest
WORKDIR /benchmark

COPY requirements.txt .
COPY . .

RUN pip --no-cache-dir install -r requirements.txt

CMD ["locust"]
