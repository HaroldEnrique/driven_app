# imagen base
FROM python:3.8.5-alpine

# estableciendo directorio de trabajo
WORKDIR /usr/src/app


# agregando e instalando requerimientos
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt


# copiando app
COPY . /usr/src/app


# ejecutando server
CMD python manage.py run -h 0.0.0.0
