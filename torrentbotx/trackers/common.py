# trackers/common.py

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class BaseTracker(ABC):
    @abstractmethod
    def search_torrents(self, keyword: str, page: int = 1, page_size: int = 5) -> Optional[Dict[str, Any]]:
        """
        搜索种子
        :param keyword: 搜索关键词
        :param page: 页码
        :param page_size: 每页的种子数量
        :return: 搜索结果字典
        """
        pass

    @abstractmethod
    def get_torrent_details(self, torrent_id: str) -> Optional[Dict[str, Any]]:
        """
        获取种子的详细信息
        :param torrent_id: 种子ID
        :return: 种子详细信息
        """
        pass

    @abstractmethod
    def get_download_link(self, torrent_id: str) -> Optional[str]:
        """
        获取种子的下载链接
        :param torrent_id: 种子ID
        :return: 下载链接
        """
        pass
