import logging
import os
from datetime import datetime

LOG_DIR="logs"
os.makedirs(LOG_DIR,exist_ok=True)


LOG_FILE = f"log_{datetime.now().strftime('%d_%m_%Y')}.log"

LOG_FILE_PATH=os.path.join(LOG_DIR,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(filename)s - %(message)s",
    datefmt="'%Y-%m-%d %H:%M:%S'"
)

RagLogger=logging.getLogger("RagLogger")