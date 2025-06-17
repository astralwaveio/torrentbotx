import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = os.path.join(os.path.dirname(__file__), '..', 'logs')
os.makedirs(LOG_DIR, exist_ok=True)

_logger_cache = {}


class Logger:
    def __init__(self, log_name='torrentbotx'):
        if log_name in _logger_cache:
            self.logger = _logger_cache[log_name]
        else:
            self.logger = logging.getLogger(log_name)
            self.logger.setLevel(logging.DEBUG)
            self._set_handlers()
            _logger_cache[log_name] = self.logger

    def _set_handlers(self):
        if self.logger.handlers:  # 避免重复添加 handler
            return

        # 控制台日志输出
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)

        # 文件日志输出
        file_handler = RotatingFileHandler(
            os.path.join(LOG_DIR, 'app.log'), maxBytes=10 * 1024 * 1024, backupCount=3, encoding='utf-8'
        )
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger


def get_logger(log_name='torrentbotx'):
    """
    获取日志实例，可自定义 log 名称
    :param log_name: 日志记录器名称，默认 'torrentbotx'
    :return: logger 实例
    """
    return Logger(log_name).get_logger()
