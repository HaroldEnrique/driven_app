# imagen base
FROM python:3.8.5-alpine

# nuevo
# install dependencies
RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd


# estableciendo directorio de trabajo
WORKDIR /usr/src/app


# agregando e instalando requerimientos
COPY ./requirements.txt /usr/src/app/requirements.txt
#RUN pip install --no-cache-dir flask
#RUN python3 -m pip install --upgrade pip
#RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#RUN pip install flask==1.1.2
#RUN pip install Flask-RESTful==0.3.8
#RUN pip install Flask-SQLAlchemy==2.4.4
#RUN pip install psycopg2-binary==2.8.6


# nuevo
# add entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh


# copiando app
COPY . /usr/src/app


# ejecutando server
CMD ["/usr/src/app/entrypoint.sh"]
#CMD python manage.py run -h 0.0.0.0

