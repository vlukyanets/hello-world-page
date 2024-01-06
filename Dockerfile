FROM python:3-alpine

WORKDIR /app

ENV BOTTOM_TEXT
ADD server.py /app

EXPOSE 8080

CMD ["python3", "server.py"]
