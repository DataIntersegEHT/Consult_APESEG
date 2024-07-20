import os
import logging
from download_csv import main_download
from consult import main_consult

# Configurar el logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Los argumentos pasados al job son accesibles a través de sys.argv
    name = os.environ.get('NAME')
    return name

if __name__ == '__main__':
    file_name = main()
    if file_name:
        main_download(file_name)
        main_consult(file_name)
    else:
        logger.info("Job terminated without processing")
