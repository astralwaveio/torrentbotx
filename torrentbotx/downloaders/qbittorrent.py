import qbittorrentapi

from torrentbotx.config.config import load_config
from torrentbotx.downloaders.base import BaseDownloader, register_downloader
from torrentbotx.enums.downloader_type import DownloaderType
from torrentbotx.utils.logger import get_logger

log = get_logger("downloaders.qbittorrent")


@register_downloader(DownloaderType.QBITTORRENT)
class QBittorrentDownloader(BaseDownloader):
    def __init__(self):
        self.config = load_config()
        self.client = None
        self.connect()

    def connect(self):
        try:
            self.client = qbittorrentapi.Client(
                host=self.config.get("QBIT_HOST", "localhost"),
                port=self.config.get("QBIT_PORT", 8080),
                username=self.config.get("QBIT_USERNAME", "admin"),
                password=self.config.get("QBIT_PASSWORD", "adminadmin")
            )
            self.client.auth_log_in()
            log.info("成功连接到 qBittorrent")
        except Exception as e:
            log.error(f"连接 qBittorrent 失败: {e}")
            raise

    def add_torrent(self, torrent_url: str) -> bool:
        try:
            self.client.torrents_add(urls=torrent_url)
            return True
        except Exception as e:
            log.error(f"添加种子失败: {e}")
            return False


class QBittorrentManager:
    """精简版的 qBittorrent 管理器, 供单元测试使用."""

    def __init__(self, api_client: qbittorrentapi.Client | None = None):
        self.api_client = api_client or qbittorrentapi.Client()

    def connect_qbit(self) -> bool:
        try:
            self.api_client.auth_log_in()
            return self.api_client.is_logged_in()
        except Exception:
            return False

    def add_torrent(self, url: str, category: str, name: str):
        return self.api_client.torrents_add(
            urls=url, category=category, rename=name, tags=[]
        )

    def remove_torrent(self, torrent_hash: str):
        return self.api_client.torrents_delete(
            torrent_hashes=torrent_hash, delete_files=False
        )

    def get_all_torrents(self):
        return self.api_client.torrents_info()


__all__ = ["QBittorrentDownloader", "QBittorrentManager"]
