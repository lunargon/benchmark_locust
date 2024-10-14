FROM python:latest
WORKDIR /benchmark

COPY requirements.txt .
COPY . .

RUN pip --no-cache-dir install -r requirements.txt

CMD ["gunicorn", "-c", "gunicorn.conf.py", "src.main:app"]
