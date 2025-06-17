from abc import ABC, abstractmethod
from typing import Dict, Type

from torrentbotx.enums.downloader_type import DownloaderType

_downloader_registry: Dict[DownloaderType, Type["BaseDownloader"]] = {}


def register_downloader(downloader_type: DownloaderType):
    def decorator(cls):
        _downloader_registry[downloader_type] = cls
        return cls

    return decorator


def get_downloader_instance(downloader_type: DownloaderType):
    cls = _downloader_registry.get(downloader_type)
    if not cls:
        raise ValueError(f"未注册下载器类型：{downloader_type}")
    return cls()


class BaseDownloader(ABC):
    @abstractmethod
    def add_torrent(self, torrent_url: str) -> bool:
        pass

    @abstractmethod
    def get_torrents(self) -> list:
        pass

    @abstractmethod
    def pause_torrent(self, torrent_id: str) -> bool:
        pass

    @abstractmethod
    def resume_torrent(self, torrent_id: str) -> bool:
        pass
