FROM python:3

WORKDIR /usr/src/app
COPY ./start.sh /start.sh
COPY . .

RUN chmod +x /start.sh
ENTRYPOINT ["/start.sh"]
