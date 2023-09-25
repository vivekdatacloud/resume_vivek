FROM python:3.9-alpine

WORKDIR /app/backend

COPY requirements.txt /app/backend
RUN pip install -r requirements.txt

COPY . /app/backend

#COPY ./entrypoint.sh /app/backend

ENTRYPOINT [ "sh", "entrypoint.sh" ]