import unittest
from unittest.mock import MagicMock
from torrentbotx.downloaders.qbittorrent import QBittorrentManager

class TestQBittorrentManager(unittest.TestCase):

    def setUp(self):
        # 设置模拟的 qBittorrent 客户端
        self.qb_api_mock = MagicMock()
        self.qb_manager = QBittorrentManager(api_client=self.qb_api_mock)

    def test_connect_qbittorrent(self):
        # 测试连接到 qBittorrent
        self.qb_api_mock.is_logged_in.return_value = True
        result = self.qb_manager.connect_qbit()
        self.assertTrue(result)
        self.qb_api_mock.auth_log_in.assert_called_once()

    def test_add_torrent(self):
        # 测试添加种子到 qBittorrent
        mock_response = {"status": "ok"}
        self.qb_api_mock.torrents_add.return_value = mock_response
        result = self.qb_manager.add_torrent("http://example.com/torrent", "Movies", "Test Torrent")
        self.assertEqual(result['status'], "ok")
        self.qb_api_mock.torrents_add.assert_called_once_with(
            urls="http://example.com/torrent", category="Movies", rename="Test Torrent", tags=[]
        )

    def test_remove_torrent(self):
        # 测试从 qBittorrent 删除种子
        mock_response = {"status": "ok"}
        self.qb_api_mock.torrents_delete.return_value = mock_response
        result = self.qb_manager.remove_torrent("12345")
        self.assertEqual(result['status'], "ok")
        self.qb_api_mock.torrents_delete.assert_called_once_with(torrent_hashes="12345", delete_files=False)

    def test_get_all_torrents(self):
        # 测试获取所有种子
        mock_response = [
            {"hash": "12345", "name": "Test Torrent", "state": "downloading"},
            {"hash": "12346", "name": "Another Torrent", "state": "paused"}
        ]
        self.qb_api_mock.torrents_info.return_value = mock_response
        result = self.qb_manager.get_all_torrents()
        self.assertEqual(len(result), 2)
        self.qb_api_mock.torrents_info.assert_called_once()

    def tearDown(self):
        # 清理资源
        del self.qb_manager
        del self.qb_api_mock
