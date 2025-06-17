import unittest
from unittest.mock import MagicMock
from torrentbotx.trackers.mteam import MTeamManager

class TestMTeamManager(unittest.TestCase):

    def setUp(self):
        # 设置模拟的 M-Team API 客户端
        self.mteam_api_mock = MagicMock()
        self.mteam_manager = MTeamManager(api_client=self.mteam_api_mock)

    def test_get_torrent_details(self):
        # 测试获取 M-Team 种子详情
        mock_response = {
            "id": "12345",
            "name": "Test Torrent",
            "smallDescr": "This is a test torrent",
            "size": 1024,
            "category": "Movies",
        }
        self.mteam_api_mock.get_torrent_details.return_value = mock_response
        result = self.mteam_manager.get_torrent_details("12345")
        self.assertEqual(result['name'], "Test Torrent")
        self.mteam_api_mock.get_torrent_details.assert_called_once_with("12345")

    def test_get_torrent_download_url(self):
        # 测试获取 M-Team 种子的下载链接
        mock_response = {
            "data": "http://example.com/download/torrent"
        }
        self.mteam_api_mock.get_torrent_download_url.return_value = mock_response
        result = self.mteam_manager.get_torrent_download_url("12345")
        self.assertEqual(result, "http://example.com/download/torrent")
        self.mteam_api_mock.get_torrent_download_url.assert_called_once_with("12345")

    def test_search_torrents_by_keyword(self):
        # 测试按关键词搜索 M-Team 种子
        mock_response = {
            "data": [
                {"id": "12345", "name": "Test Torrent", "smallDescr": "Test description"},
                {"id": "12346", "name": "Another Test Torrent", "smallDescr": "Another description"}
            ],
            "total": 2,
            "pageNumber": 1,
            "totalPages": 1
        }
        self.mteam_api_mock.search_torrents_by_keyword.return_value = mock_response
        result = self.mteam_manager.se_
