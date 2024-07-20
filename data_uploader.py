import io
import json
from fastavro.schema import load_schema
from fastavro import writer, parse_schema
from google.cloud import storage
from datetime import datetime
import logging

# Obtener el periodo
period = datetime.now().strftime("%Y%m")
# Configurar el registro
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def save_to_avro(datos, numero_placa, bucket_name, schema_path):
    try:
        #logger.info(f"Iniciando proceso de guardado en Avro para la placa: {numero_placa}")

        # Cargar el esquema usando fastavro
        with open(schema_path, 'r') as f:
            schema = json.load(f)
        schema = parse_schema(schema)
        #logger.info(f"Esquema cargado y parseado desde: {schema_path}")

        # Verificar el tipo de datos
        if not isinstance(datos, list):
            raise ValueError("Los datos deben ser una lista de diccionarios.")
        for item in datos:
            if not isinstance(item, dict):
                raise ValueError("Cada item en los datos debe ser un diccionario.")

        # Crear un buffer en memoria
        output = io.BytesIO()

        # Convertir los datos a formato bytes usando fastavro
        writer(output, schema, datos)
        #logger.info("Datos escritos en el buffer en formato Avro")

        # Posicionar el buffer al principio
        output.seek(0)

        # Crear un cliente de Google Cloud Storage
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        #logger.info(f"Cliente de Google Cloud Storage creado para el bucket: {bucket_name}")

        # Definir la ruta del archivo en el bucket para el archivo Avro principal
        ruta_archivo_principal = f"PRD/APESEG/APESEG_RECUPERACION/PERIODO={period}/apesegsoat_{numero_placa}.avro"
        blob_principal = bucket.blob(ruta_archivo_principal)

        # Subir el archivo Avro principal desde el buffer
        blob_principal.upload_from_file(output, content_type='application/octet-stream')
        logger.info(f"Archivo principal subido a gs://{bucket_name}/{ruta_archivo_principal}")

    except Exception as e:
        logger.warning(f"Error al escribir o subir el archivo de datos adicionales: {e}")

