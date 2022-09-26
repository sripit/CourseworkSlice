#difference from this to original dockerfile:
    #added a CMD to run Gunicorn
    #two ner environment vairbales
    #created and switched to a non-root user
    #made out web app listen on a particular port  calledm $PORT
# pull official base image
FROM python:3.10.3-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_ENV production
ENV APP_SETTINGS src.config.ProductionConfig

ARG SECRET_KEY
ENV SECRET_KEY $SECRET_KEY
# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# add and install requirements
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# add app
COPY . .

# add and run as non-root user
RUN adduser --disabled-password myuser
USER myuser

# run gunicorn
CMD gunicorn --bind 0.0.0.0:$PORT manage:app