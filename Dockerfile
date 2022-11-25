# Imagen base
FROM python:3.11-alpine

# Establecer directorio de trabajo
WORKDIR /code 

#Establece dos variables de entorno con los siguientes valores: 
ENV FLASK_APP=app.py 
ENV FLASK_RUN_HOST=0.0.0.0 

# Descargar e instalar dependencias
RUN apk add --no-cache gcc musl-dev linux-headers

COPY ./requirements.txt /code

# Descargar e instalar dependencias
RUN pip install -r requirements.txt

EXPOSE 5000
COPY ./app.py /code

# Comando de arranque
CMD flask run