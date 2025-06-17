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

    def get_torrents(self):
        try:
            return self.client.torrents_info()
        except Exception as e:
            log.error(f"获取种子失败: {e}")
            return []

    def pause_torrent(self, torrent_hash: str) -> bool:
        try:
            self.client.torrents_pause(torrent_hashes=[torrent_hash])
            return True
        except Exception as e:
            log.error(f"暂停失败: {e}")
            return False

    def resume_torrent(self, torrent_hash: str) -> bool:
        try:
            self.client.torrts_resume(torrent_hashes=[torrent_hash])
            return True
        except Exception as e:
            log.error(f"恢复失败: {e}")
            return False
