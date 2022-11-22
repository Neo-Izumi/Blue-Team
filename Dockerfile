FROM python:3.10

RUN mkdir -p /blue_bot

WORKDIR /blue_bot

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "main.py" ]