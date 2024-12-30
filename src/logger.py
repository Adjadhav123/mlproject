# import logging 
# import os 
# from datetime import datetime
# LOG_DIR = "logs"
# os.makedirs(LOG_DIR, exist_ok=True)

# LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
# LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[%(actime)s %(lineno)d %(name)s - %(levelname)s -%(message)s]",
#     level=logging.INFO,
# )


# if __name__=="__main__":
#     logging.info("Logging has started")



import logging
import os
from datetime import datetime

# Create logs directory
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Create log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Construct the log file path correctly
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")