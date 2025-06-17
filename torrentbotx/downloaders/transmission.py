import transmission_rpc

from torrentbotx.config.config import load_config
from torrentbotx.downloaders.base import BaseDownloader, register_downloader
from torrentbotx.enums.downloader_type import DownloaderType
from torrentbotx.utils.logger import get_logger

log = get_logger("downloaders.transmission")


@register_downloader(DownloaderType.TRANSMISSION)
class TransmissionDownloader(BaseDownloader):
    def __init__(self):
        self.config = load_config()
        self.client = None
        self.connect()

    def connect(self):
        try:
            self.client = transmission_rpc.Client(
                username=self.config.get("TRANSMISSION_USER", "admin"),
                password=self.config.get("TRANSMISSION_PASSWORD", "password"),
                host=self.config.get("TRANSMISSION_HOST", "127.0.0.1"),
                port=self.config.get("TRANSMISSION_PORT", 9091),
                path=self.config.get("TRANSMISSION_PATH", "/transmission/rpc"),
                timeout=self.config.get("TRANSMISSION_TIME_OUT", 5000),
                logger=log
            )
            log.info("成功连接到 Transmission")
        except Exception as e:
            log.error(f"连接 Transmission 错误: {e}")
            raise

    def add_torrent(self, torrent_url: str) -> bool:
        try:
            self.client.add_torrent(torrent_url)
            return True
        except Exception as e:
            log.error(f"添加种子失败: {e}")
            return False

    def get_torrents(self):
        try:
            return self.client.get_torrents()
        except Exception as e:
            log.error(f"获取任务失败: {e}")
            return []

    def pause_torrent(self, torrent_id: str) -> bool:
        try:
            self.client.stop_torrent(torrent_id)
            return True
        except Exception as e:
            log.error(f"暂停任务失败: {e}")
            return False

    def resume_torrent(self, torrent_id: str) -> bool:
        try:
            self.client.start_torrent(torrent_id)
            return True
        except Exception as e:
            log.error(f"恢复任务失败: {e}")
            return False
