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

def setup_logging():
    # Create logs directory if it doesn't exist
    logs_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(logs_dir, exist_ok=True)

    # Create log file name with timestamp
    log_filename = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
    log_filepath = os.path.join(logs_dir, log_filename)

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_filepath),
            logging.StreamHandler()
        ]
    )

    # Test log message
    # logging.info("Logging has been initialized")

if __name__ == "__main__":
    setup_logging()
