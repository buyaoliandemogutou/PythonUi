import os
import logging
import threading
from logging.handlers import TimedRotatingFileHandler
import time

#log_path = os.path.join(path, 'result')  # 存放log文件的路径
path = '../Result'
class Logger(object):
    def __init__(self, logger_name='logs'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        self.log_file_name = 'logs.' + time.strftime("%Y-%m-%d", time.localtime())# 日志文件的名称
        self.backup_count = 5  #最多存放日志的数量
        # 日志输出级别
        self.console_output_level = 'WARNING'
        self.file_output_level = 'DEBUG'
        # 日志输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        if not self.logger.handlers:  # 避免重复日志
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            file_handler = TimedRotatingFileHandler(filename=os.path.join(path, self.log_file_name), when='D',
                                                    interval=1, backupCount=self.backup_count, delay=True,
                                                    encoding='utf-8')
            print(file_handler)
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger

logger = Logger().get_logger()
class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Logger()
            MyLog.mutex.release()
        return MyLog.log

if __name__ == "__main__":
    log = MyLog.get_log()
    logger = log.get_logger()
    logger.debug("test debug")
    logger.info("test info")
