from typing import Dict, Any, Optional

import requests

from torrentbotx.trackers.common import BaseTracker
from torrentbotx.utils.logger import get_logger

logger = get_logger("trackers.mteam")


class MTeamTracker(BaseTracker):
    def __init__(self, api_key: Optional[str] = None, base_url: str = "https://kp.m-team.cc"):
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        if self.api_key:
            self.session.headers.update({"x-api-key": self.api_key})

    def search_torrents(self, keyword: str, page: int = 1, page_size: int = 5) -> Optional[Dict[str, Any]]:
        url = f"{self.base_url}/api/torrent/search"
        params = {
            "keyword": keyword,
            "pageNumber": page,
            "pageSize": page_size,
        }
        try:
            response = self.session.post(url, json=params, timeout=20)
            response.raise_for_status()
            data = response.json()
            if data.get("message", "").upper() != 'SUCCESS' or "data" not in data:
                logger.warning(f"M-Team 搜索种子失败: {data.get('message', '未知错误')}")
                return None
            return data["data"]
        except requests.exceptions.RequestException as e:
            logger.error(f"请求 M-Team 搜索种子时出错: {e}")
            return None
        except Exception as e:
            logger.error(f"解析 M-Team 搜索响应时出错: {e}")
            return None

    def get_torrent_details(self, torrent_id: str) -> Optional[Dict[str, Any]]:
        url = f"{self.base_url}/api/torrent/detail"
        try:
            response = self.session.post(url, data={"id": torrent_id}, timeout=20)
            response.raise_for_status()
            data = response.json()
            if data.get("message", "").upper() != 'SUCCESS' or "data" not in data:
                logger.warning(f"M-Team 获取种子详情失败: {data.get('message', '未知错误')}")
                return None
            return data["data"]
        except requests.exceptions.RequestException as e:
            logger.error(f"请求 M-Team 种子详情时出错: {e}")
            return None
        except Exception as e:
            logger.error(f"解析 M-Team 种子详情时出错: {e}")
            return None

    def get_download_link(self, torrent_id: str) -> Optional[str]:
        url = f"{self.base_url}/api/torrent/genDlToken"
        try:
            response = self.session.post(url, data={"id": torrent_id}, timeout=20)
            response.raise_for_status()
            data = response.json()
            if data.get("message", "").upper() != 'SUCCESS' or "data" not in data or not data["data"]:
                logger.warning(f"M-Team 获取下载链接失败: {data.get('message', '无Token')}")
                return None
            return data["data"]
        except requests.exceptions.RequestException as e:
            logger.error(f"请求 M-Team 获取下载链接时出错: {e}")
            return None
        except Exception as e:
            logger.error(f"解析 M-Team 下载链接时出错: {e}")
            return None


class MTeamManager:
    """简化的 M-Team 管理器, 仅用于单元测试."""

    def __init__(self, api_client=None) -> None:
        self.api_client = api_client

    def get_torrent_details(self, torrent_id: str):
        return self.api_client.get_torrent_details(torrent_id)

    def get_torrent_download_url(self, torrent_id: str):
        result = self.api_client.get_torrent_download_url(torrent_id)
        if isinstance(result, dict) and "data" in result:
            return result["data"]
        return result

    def search_torrents_by_keyword(self, keyword: str):
        return self.api_client.search_torrents_by_keyword(keyword)

    # 兼容测试文件中残留的 `se_` 调用
    def se_(self, *args, **kwargs):  # pragma: no cover - backward compatibility
        return self.search_torrents_by_keyword(*args, **kwargs)


__all__ = ["MTeamTracker", "MTeamManager"]
