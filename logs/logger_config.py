import logging
import logging.config


class LoggerConf:

    @staticmethod
    def test():
        # create logger
        logging.config.fileConfig('logger.conf')
        logger = logging.getLogger(LoggerConf.__name__)

        # logging messages
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')


LoggerConf.test()
