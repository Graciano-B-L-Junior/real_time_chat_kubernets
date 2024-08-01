FROM mysql:9

ENV MYSQL_ROOT_PASSWORD=root

WORKDIR /db_files

COPY ./users_db.sql /docker-entrypoint-initdb.d/

