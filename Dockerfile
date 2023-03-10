# pull official base image
FROM python:3.9-slim


# set work directory
WORKDIR /twitter-stream-api


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# EXPOSE 9000

COPY . /twitter-stream-api


# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9000"]
