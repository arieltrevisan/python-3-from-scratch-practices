import logging


class Logger:

    @staticmethod
    def test():
        # create logger
        logger = logging.getLogger(Logger.__name__)
        # logger.setLevel(logging.INFO)

        # create console handler and set level to info
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                      datefmt='%Y/%m/%d %H:%M:%S %Z')

        # add formatter to console handler
        console_handler.setFormatter(formatter)

        # add console handler to logger
        logger.addHandler(console_handler)

        # logging messages
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')


Logger.test()
