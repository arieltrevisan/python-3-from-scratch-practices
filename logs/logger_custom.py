import logging
from logs import logger_custom_module as cl


class CustomLogDemo:
    log = cl.create_logger(logging.INFO)

    def method_1(self):
        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warning('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

    def method_2(self):
        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warning('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

    def method_3(self):
        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warning('warn message')
        self.log.error('error message')
        self.log.critical('critical message')


t1 = CustomLogDemo()
t1.method_1()
t1.method_2()
t1.method_3()
