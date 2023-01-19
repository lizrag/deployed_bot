FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python3", "dolar.py", "repote.py","telegram.py", "--host=0.0.0.0", "--port=5000"]