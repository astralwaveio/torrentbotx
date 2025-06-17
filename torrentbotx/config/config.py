import os
from pathlib import Path
from typing import Any, Dict

import yaml

from torrentbotx.utils.logger import get_logger

# 获取日志记录器
logger = get_logger()

# 默认配置项
DEFAULT_CONFIG = {
    'QBIT_HOST': 'localhost',
    'QBIT_PORT': 8080,
    'QBIT_USERNAME': 'admin',
    'QBIT_PASSWORD': 'adminadmin',
    'TG_BOT_TOKEN': '',
    'MT_HOST': 'https://api.m-team.cc',
    'MT_APIKEY': '',
    'USE_IPV6_DOWNLOAD': False,
    'LOCAL_TIMEZONE': 'Asia/Shanghai',
}

# 默认配置文件路径
DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.yaml')
EXAMPLE_CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'example.yaml')


class Config:
    def __init__(self, config_file: str = DEFAULT_CONFIG_PATH):
        """
        初始化配置，支持从配置文件加载配置项。配置加载顺序：环境变量 > 配置文件 > 默认值。
        :param config_file: 配置文件路径，默认为 'config.yaml'。
        """
        self.config_file = config_file
        self.config_data = self._load_config(config_file)
        self._load_from_env()  # 从环境变量加载配置，覆盖配置文件中的配置
        self._validate_config()

    @staticmethod
    def _load_config(config_file: str) -> Dict[str, Any]:
        """
        从指定的 YAML 配置文件加载配置。
        :param config_file: 配置文件路径
        :return: 配置字典
        """
        config_data = DEFAULT_CONFIG.copy()  # 默认配置
        if Path(config_file).exists():
            try:
                with open(config_file, 'r', encoding='utf-8') as file:
                    file_data = yaml.safe_load(file) or {}
                    config_data.update(file_data)
                    logger.info(f"成功加载配置文件: {config_file}")
            except yaml.YAMLError as e:
                logger.error(f"读取配置文件 {config_file} 时出错：{e}")
                raise
            except Exception as e:
                logger.error(f"加载配置文件 {config_file} 时发生未知错误：{e}")
                raise
        else:
            logger.warning(f"配置文件 {config_file} 不存在，使用默认配置")

        return config_data

    def _load_from_env(self):
        """
        从环境变量加载配置项，如果环境变量存在则覆盖配置文件中的配置。
        """
        for key in self.config_data:
            env_value = os.getenv(key)
            if env_value is not None:
                # 转换为正确的数据类型（例如整数、布尔值等）
                if env_value.lower() == 'false':
                    self.config_data[key] = False
                elif env_value.lower() == 'true':
                    self.config_data[key] = True
                elif key == 'QBIT_PORT' or key == 'MT_APIKEY':
                    self.config_data[key] = int(env_value) if env_value.isdigit() else env_value
                else:
                    self.config_data[key] = env_value
                logger.info(f"加载环境变量配置：{key} = {env_value}")

    def _validate_config(self):
        """
        验证配置的完整性，确保所有必要的配置项存在。
        """
        required_keys = ['QBIT_HOST', 'QBIT_PORT', 'QBIT_USERNAME', 'QBIT_PASSWORD', 'TG_BOT_TOKEN']
        for key in required_keys:
            if not self.config_data.get(key):
                logger.warning(f"配置文件缺少必需的键：{key}")

    def get(self, key: str, default: Any = None) -> Any:
        """
        获取配置项的值
        :param key: 配置项键
        :param default: 默认值（当键不存在时返回）
        :return: 配置项的值
        """
        return self.config_data.get(key, default)

    def get_all(self) -> Dict[str, Any]:
        """
        获取所有配置项
        :return: 配置项字典
        """
        return self.config_data

    def set(self, key: str, value: Any) -> None:
        """
        设置某个配置项的值
        :param key: 配置项键
        :param value: 配置项值
        """
        self.config_data[key] = value

    def save(self) -> None:
        """
        保存当前配置到文件
        """
        try:
            with open(self.config_file, 'w', encoding='utf-8') as file:
                yaml.dump(self.config_data, file, default_flow_style=False, allow_unicode=True)
            logger.info(f"配置已成功保存到 {self.config_file}")
        except Exception as e:
            logger.error(f"保存配置文件时出错：{e}")


# 配置文件加载函数
def load_config(config_file: str = DEFAULT_CONFIG_PATH) -> Config:
    """
    加载配置
    :param config_file: 配置文件路径，默认为 'config.yaml'
    :return: 配置对象
    """
    return Config(config_file)
