from typing import Optional, List

from torrentbotx.config.config import load_config
from torrentbotx.downloaders.base import get_downloader_instance
from torrentbotx.enums.downloader_type import DownloaderType
from torrentbotx.notifications import Notifier
from torrentbotx.notifications.telegram_notifier import TelegramNotifier
from torrentbotx.utils import get_logger

logger = get_logger("core.manager")


class CoreManager:
    def __init__(self, config=None, notifier: Optional[Notifier] = None):
        self.config = config or load_config()
        self.notifier = notifier or TelegramNotifier(
            bot_token=self.config.get("TG_BOT_TOKEN"),
            chat_id=self.config.get("TG_ALLOWED_CHAT_IDS")
        )
        self.downloaders = self._init_downloaders()

    def _init_downloaders(self) -> List:
        types = self.config.get("DOWNLOADERS", "qbittorrent")
        downloader_list = []
        for name in types.split(","):
            try:
                dtype = DownloaderType.from_name(name.strip())
                instance = get_downloader_instance(dtype)
                downloader_list.append(instance)
            except Exception as e:
                logger.error(f"❌ 加载下载器 {name} 失败: {e}")
        return downloader_list

    def start(self):
        logger.info("🎯 正在启动 CoreManager ...")
        if not self.downloaders:
            logger.warning("⚠️ 未加载任何下载器，请检查配置 DOWNLOADERS")
        else:
            logger.info(f"✅ 加载下载器数量: {len(self.downloaders)}")

        if not self.config.get("TG_BOT_TOKEN"):
            logger.warning("⚠️ 未配置 TG_BOT_TOKEN，无法发送 Telegram 通知")

        self.notifier.send_message("CoreManager 启动完成 ✅")

    def execute_download_task(self, params: dict):
        torrent_id = params.get("torrent_id")
        if not torrent_id:
            logger.error("🚫 下载任务缺少 Torrent ID 参数")
            return False

        logger.info(f"🔄 正在下载种子：{torrent_id}")
        success_list = []
        for downloader in self.downloaders:
            success = downloader.add_torrent(torrent_id)
            success_list.append(success)

        if any(success_list):
            self.notifier.send_message(f"部分下载器已成功添加任务: {torrent_id}")
            return True
        else:
            self.notifier.send_message(f"所有下载器添加任务失败: {torrent_id}")
            return False


class TorrentManager:
    """简化的种子管理器，用于测试目的."""

    def __init__(self, qb_client=None) -> None:
        self.qb_client = qb_client

    def add_torrent(self, torrent_url: str) -> None:
        if not self.qb_client:
            raise RuntimeError("qBittorrent client 未初始化")
        self.qb_client.torrents_add(urls=torrent_url)

    def get_torrent(self, torrent_hash: str):
        if not self.qb_client:
            raise RuntimeError("qBittorrent client 未初始化")
        return self.qb_client.torrents_info(torrent_hashes=torrent_hash)
