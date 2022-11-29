# Imagen base
FROM python:3.7-alpine

# Establecer directorio de trabajo
WORKDIR /code 

COPY ./requirements.txt /code

# Descargar e instalar dependencias
RUN pip install -r requirements.txt

COPY ./app.py /code

# Comando de arranque
CMD ["python","/code/app.py"]
