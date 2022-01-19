import logging
from pathlib import Path
from logging.handlers import RotatingFileHandler


def create_logger(log_folder: str) -> logging.getLogger:
    """
    To create logger and save in defined log folder
    :param log_folder: folder name to save log files
    :return: logging object
    """
    Path(log_folder).mkdir(parents=True, exist_ok=True)  # create folder if not exists
    handler = RotatingFileHandler(log_folder + '/access.logs',
                                  maxBytes=10000000, backupCount=5)
    logger = logging.getLogger('reporting-tools-info')
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger
