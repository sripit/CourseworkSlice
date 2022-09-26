#extended the official Postgres image by adding create.sql
#to "docker-entrypoint-initdb.d" directory in the container

#pull official base image
FROM postgres:14-alpine

#run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d