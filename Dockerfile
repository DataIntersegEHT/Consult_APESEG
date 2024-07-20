# Utilice la imagen oficial ligera de Python de Docker Hub
# https://hub.docker.com/_/python
FROM python:3.9-slim

# Establecer variable de entorno
ENV PORT 8080

# Permitir que las declaraciones y los mensajes de registro aparezcan inmediatamente en los registros de Knative
ENV PYTHONUNBUFFERED True

# Copiar todo
WORKDIR /app
COPY . .

# Instalar dependencias
#RUN pip install Flask gunicorn google-cloud-storage
RUN pip install --no-cache-dir -r requirements.txt

# Run the web service on container startup.
CMD ["python3","app.py"]