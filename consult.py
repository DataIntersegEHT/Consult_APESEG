import csv
import logging
from api_connector import get_data
from data_uploader import save_to_avro

# Configurar el registro
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main(vehicle_plate, bucket_name, schema_path):
    try:
        #logger.info(f"Obteniendo datos para la placa: {vehicle_plate}")
        # Obtener datos de la API
        
        data = get_data(vehicle_plate)
        #logger.info(f'====>{vehicle_plate}====>{data}')
        #logger.info(f"Guardando datos en Avro y subiendo al bucket: {bucket_name}")
        # Guardar los datos en Avro y subirlos al bucket
        save_to_avro(data, vehicle_plate, bucket_name, schema_path)
    except Exception as e:
        logger.warning(f"Error en main para la placa {vehicle_plate}: {e}")

def leer_placas_de_csv(ruta_csv):
    try:
        with open(ruta_csv, newline='') as csvfile:
            reader = csv.reader(csvfile)
            placas = [fila[0] for fila in reader]
        #logger.info(f"Placas leídas del archivo CSV {ruta_csv}: {placas}")
        return placas
    except FileNotFoundError:
        logger.warning(f"El archivo {ruta_csv} no fue encontrado.")
        return []
    except Exception as e:
        logger.warning(f"Error al leer el archivo CSV {ruta_csv}: {e}")
        return []

def main_consult(file):
    try:
        # Parámetros de configuración
        bucket_name = 'interseguro-datalake-prd-landing'
        schema_path = './schema.avsc'
        fil = file.split("/")[-1]
        ruta_csv = f'./data/{fil}'
        
        #logger.info(f"Leyendo placas del archivo CSV: {ruta_csv}")
        # Leer placas del archivo CSV
        placas = leer_placas_de_csv(ruta_csv)
        
        for placa in placas:
            main(placa, bucket_name, schema_path)
    except Exception as e:
        logger.warning(f"Error en main_consult para el archivo {file}: {e}")