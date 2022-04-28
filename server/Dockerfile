FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN ls -la

RUN pip install -r requirements.txt

COPY . .

RUN chmod 777 /app

CMD [ "python", "main.py"]
