"""Configuration loader for TorrentBotX."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict

import yaml
from pydantic_settings import BaseSettings

from torrentbotx.utils.logger import get_logger

logger = get_logger("config")

DEFAULT_CONFIG_PATH = Path(__file__).with_name("config.yaml")
EXAMPLE_CONFIG_PATH = Path(__file__).with_name("example.yaml")
CONFIG_ENV_VAR = "TORRENTBOTX_CONFIG"


class Settings(BaseSettings):
    """Typed settings with environment variable support."""

    QBIT_HOST: str = "localhost"
    QBIT_PORT: int = 8080
    QBIT_USERNAME: str = "admin"
    QBIT_PASSWORD: str = "adminadmin"
    TG_BOT_TOKEN: str = ""
    MT_HOST: str = "https://api.m-team.cc"
    MT_APIKEY: str = ""
    USE_IPV6_DOWNLOAD: bool = False
    LOCAL_TIMEZONE: str = "Asia/Shanghai"

    class Config:
        env_prefix = ""
        case_sensitive = False


class Config:
    """Wrapper around :class:`Settings` for backward compatibility."""

    def __init__(self, config_file: str | Path | None = None) -> None:
        self.config_file = Path(
            config_file or os.getenv(CONFIG_ENV_VAR, DEFAULT_CONFIG_PATH)
        )
        data = self._load_yaml(self.config_file)
        self.settings = Settings(**data)
        self._validate_config()

    @staticmethod
    def _load_yaml(path: Path) -> Dict[str, Any]:
        data: Dict[str, Any] = {}
        if path.exists():
            try:
                with open(path, "r", encoding="utf-8") as fh:
                    file_data = yaml.safe_load(fh) or {}
                    data.update(file_data)
                logger.info("成功加载配置文件: %s", path)
            except Exception as exc:  # pragma: no cover - unexpected IO errors
                logger.error("读取配置文件 %s 时出错：%s", path, exc)
                raise
        else:
            logger.warning("配置文件 %s 不存在，使用默认配置", path)
        return data

    def _validate_config(self) -> None:
        required_keys = [
            "QBIT_HOST",
            "QBIT_PORT",
            "QBIT_USERNAME",
            "QBIT_PASSWORD",
            "TG_BOT_TOKEN",
        ]
        for key in required_keys:
            if not getattr(self.settings, key, None):
                logger.warning("配置文件缺少必需的键：%s", key)

    def get(self, key: str, default: Any = None) -> Any:
        return getattr(self.settings, key, default)

    def get_all(self) -> Dict[str, Any]:
        return self.settings.dict()

    def set(self, key: str, value: Any) -> None:
        setattr(self.settings, key, value)

    def reload(self) -> None:
        data = self._load_yaml(self.config_file)
        self.settings = Settings(**data)

    def save(self) -> None:
        try:
            with open(self.config_file, "w", encoding="utf-8") as fh:
                yaml.dump(
                    self.settings.dict(),
                    fh,
                    default_flow_style=False,
                    allow_unicode=True,
                )
            logger.info("配置已成功保存到 %s", self.config_file)
        except Exception as exc:  # pragma: no cover - unexpected IO errors
            logger.error("保存配置文件时出错：%s", exc)


def load_config(config_file: str | Path | None = None) -> Config:
    """Convenient helper to load configuration."""

    return Config(config_file)
