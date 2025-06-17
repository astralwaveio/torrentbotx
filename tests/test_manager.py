import unittest
from torrentbotx.core.manager import TorrentManager
from unittest.mock import MagicMock

class TestTorrentManager(unittest.TestCase):

    def setUp(self):
        # 模拟客户端与其他服务
        self.manager = TorrentManager()
        self.qb_client_mock = MagicMock()
        self.manager.qb_client = self.qb_client_mock

    def test_add_torrent(self):
        # 测试添加种子任务
        torrent_url = "http://example.com/torrent"
        self.manager.add_torrent(torrent_url)
        self.qb_client_mock.torrents_add.assert_called_once_with(urls=torrent_url)

    def test_get_torrent(self):
        # 测试获取种子任务
        torrent_hash = "abcd1234"
        self.manager.get_torrent(torrent_hash)
        self.qb_client_mock.torrents_info.assert_called_once_with(torrent_hashes=torrent_hash)

    def tearDown(self):
        # 清理资源
        del self.manager
        del self.qb_client_mock
