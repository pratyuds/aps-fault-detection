import logging
import os
from datetime import datetime

# log file name
LOG_FILE_NAME =f"{datetime.now().strftime('%Y-%m-%d')}.log"

#Log directory
LOG_FILE_DIR = os.path.join(os.getcwd(),"logs")

# create folder if not available
os.makedirs(LOG_FILE_DIR,exist_ok=True)

#log file path
LOG_FILE_PATH = logging.basicConfig(
    filename=LOG_FILE_NAME,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)