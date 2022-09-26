#pull official base image
FROM postgres:14-alpine
#run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d
#extended the official postgres image by adding create.sql to the docker-entrypoint