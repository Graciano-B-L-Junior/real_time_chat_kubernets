FROM python:3.10-bullseye

WORKDIR /app

COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "app.py" ]