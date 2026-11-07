import os
import logging

#create log directy
os.makedirs("logs", exist_ok=True)


#configure logging
logging.basicConfig(
    level =logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)

#create logger
logger = logging.getLogger("CoforgeCustomerDB")