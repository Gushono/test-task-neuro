import logging
import os
from logging.handlers import RotatingFileHandler

LOGGER_NAME = "test_logger"


def factory_logger():
    if not os.path.exists("./logs"):
        os.makedirs("./logs")

    logging.basicConfig(level=logging.INFO)

    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(level=logging.INFO)

    handler_local = RotatingFileHandler(
        f"./logs/{__name__}.log", mode="a", maxBytes=50000, backupCount=10
    )
    formatter = logging.Formatter(
        "[%(levelname)s] %(asctime)s %(funcName)s -> %(message)s"
    )

    handler_local.setFormatter(formatter)
    logger.addHandler(handler_local)

    return logger


def get_logger():
    logger = logging.getLogger(LOGGER_NAME)
    return logger
