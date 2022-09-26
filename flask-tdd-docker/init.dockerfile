# pull official base image
    #baseimage: image used to clean all container images
    #docker container image: a lightweight standalone executable
    #package of software that includes everything needed to run an
    #application
FROM python:3.10.3-slim-buster

#why do you need to set a working directory?
# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
#PYTHONDONTWRITEBYTECODE: Prevents python from writing pyc files to disc
    #pyc files: compiled output file generated from source code written
    #in Python
#PYTHONBUFFERED: Prevents Python from buffrering stdout and stderr
    #stdout: the standard output stream: a source of output from the program
    #stderr: standard error stream. used for error messages
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean \

# add and install requirements
RUN pip install --upgrade pip
COPY ./requirements.txt .
COPY ./requirements-dev.txt .
RUN pip install -r requirements-dev.txt


# add app
COPY . .

# add entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh
