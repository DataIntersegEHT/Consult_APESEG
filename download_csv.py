from google.cloud import storage
from google.cloud import exceptions
import logging

# Configurar el registro
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def download_csv(bucket_name, archivo_gs, archivo_local):
    try:
        # Inicializar el cliente de Cloud Storage
        client = storage.Client()

        # Obtener el bucket
        bucket = client.bucket(bucket_name)

        # Descargar el archivo
        blob = bucket.blob(archivo_gs)
        blob.download_to_filename(archivo_local)

        # Registrar información de éxito
        #logger.info(f"file {archivo_gs} downloaded locally as {archivo_local}")
    except exceptions.NotFound:
        logger.error(f"The bucket {bucket_name} or blob {archivo_gs} does not exist.")
    except exceptions.GoogleCloudError as e:
        logger.error(f"An error occurred with Google Cloud Storage: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

def main_download(file):
    try:
        bucket_name = "interseguro-datalake-prd-landing"
        archivo_gs = file
        name_file = archivo_gs.split('/')[-1]
        archivo_local = f"./data/{name_file}"

        download_csv(bucket_name, archivo_gs, archivo_local)
    except Exception as e:
        logger.error(f"An error occurred in main_download: {e}")