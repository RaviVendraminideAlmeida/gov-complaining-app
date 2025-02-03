FROM python:3.9

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

EXPOSE 3333

CMD ["fastapi", "run", "./main.py", "--port", "3333"]