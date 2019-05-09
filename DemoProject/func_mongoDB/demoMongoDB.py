import os
from common.logger import get_logger
from pymongo import MongoClient

logger = get_logger(os.path.splitext(os.path.basename(__file__))[0])


def demo():
    logger.info("Demo START")

    client = MongoClient('127.0.0.1', 27017)
    # client = MongoClient('mongodb://localhost:27017/')
    db = client.test
    collection = db.MyCollection

    print(db)
    print(collection)
    print(collection.stats)
    for record in collection.find().limit(10):
        logger.info(record)

    logger.info("Demo END")
