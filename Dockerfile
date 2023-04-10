FROM python:3.8-slim-buster
WORKDIR /code
COPY . .
CMD ["python3", "main.py"]
