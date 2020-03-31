FROM python:3.7-alpine

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


ENTRYPOINT [ "python" ]

CMD [ "app.py" ]

