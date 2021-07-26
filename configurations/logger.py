import logging
import os
from logging.handlers import RotatingFileHandler

LOGGER_NAME = "logger_neuro"


def factory_logger() -> logging.Logger:
    """
    Function responsable to fabricate the logger and configure him
    """
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


def get_logger() -> logging.Logger:
    """
    Function responsable to GET the logger that are already created
    """

    logger = logging.getLogger(LOGGER_NAME)
    return logger
