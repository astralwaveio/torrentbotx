import aria2p

from torrentbotx.config.config import load_config
from torrentbotx.downloaders.base import BaseDownloader, register_downloader
from torrentbotx.enums.downloader_type import DownloaderType
from torrentbotx.utils.logger import get_logger

logger = get_logger("downloaders.aria2")


@register_downloader(DownloaderType.ARIA2)
class Aria2Downloader(BaseDownloader):
    def __init__(self):
        self.config = load_config()
        self.client = None
        self.connect()

    def connect(self):
        try:
            self.client = aria2p.API(aria2p.Client(
                host=self.config.get("ARIA2_HOST", "http://localhost"),
                port=self.config.get("ARIA2_PORT", 6800)))
            logger.info("成功连接到 Aria2")
        except Exception as e:
            logger.error(f"连接 Aria2 错误: {e}")
            raise

    def add_torrent(self, torrent_url: str) -> bool:
        try:
            self.client.add_torrent(torrent_url)
            return True
        except Exception as e:
            logger.error(f"添加 Aria2 种子失败: {e}")
            return False

    def get_torrents(self):
        try:
            return self.client.get_downloads()
        except Exception as e:
            logger.error(f"获取 Aria2 下载任务失败: {e}")
            return []

    def pause_torrent(self, torrent_id: str) -> bool:
        try:
            self.client.pause(torrent_id)
            return True
        except Exception as e:
            logger.error(f"暂停 Aria2 下载任务失败: {e}")
            return False

    def resume_torrent(self, torrent_id: str) -> bool:
        try:
            self.client.unpause(torrent_id)
            return True
        except Exception as e:
            logger.error(f"恢复 Aria2 下载任务失败: {e}")
            return False
