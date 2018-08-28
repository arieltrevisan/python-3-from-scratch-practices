import inspect
import logging


def create_logger(log_level):
    logger_name = inspect.stack()[1][3]

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(filename="{0}.log".format(logger_name))
    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%Y/%m/%d %H:%M:%S %Z')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
