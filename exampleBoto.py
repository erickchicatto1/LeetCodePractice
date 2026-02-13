import boto3
import logging
from botocore import UNSIGNED
from botocore.config import Config
from botocore.exceptions import BotoCoreError, ClientError
from typing import Optional

# Configuración centralizada
BUCKET_NAME = "coderbytechallengesandbox"
FILE_PREFIX = "_cb_"
CHALLENGE_TOKEN = "mz1lp3xgla6"

# Configuración de logging para producción
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def get_first_matching_file(bucket: str, prefix: str) -> Optional[str]:
    """
    Obtiene el nombre del primer archivo que coincide con el prefijo 
    utilizando filtrado del lado del servidor.
    """
    try:
        s3 = boto3.client("s3", config=Config(signature_version=UNSIGNED))
        
        # Usamos Prefix para que S3 filtre por nosotros (más eficiente)
        response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix, MaxKeys=1)
        
        contents = response.get("Contents")
        if not contents:
            return None
            
        return contents[0]["Key"]

    except (BotoCoreError, ClientError) as e:
        logger.error(f"Error al conectar con S3: {e}")
        return None

def transform_string_with_token(text: str, token: str) -> str:
    """
    Reemplaza caracteres presentes en el token por guiones.
    Optimizado usando un set para búsquedas rápidas.
    """
    token_set = set(token)
    return "".join("-" if char in token_set else char for char in text)

def main():
    file_name = get_first_matching_file(BUCKET_NAME, FILE_PREFIX)
    
    if not file_name:
        logger.warning("No se encontró ningún archivo que coincida con el criterio.")
        return

    result = transform_string_with_token(file_name, CHALLENGE_TOKEN)
    print(result)

if __name__ == "__main__":
    main()
