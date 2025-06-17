import unittest
from torrentbotx.utils import Utility

class TestUtility(unittest.TestCase):

    def setUp(self):
        # 在每个测试之前初始化需要的内容
        self.utility = Utility()

    def test_format_bytes(self):
        # 测试格式化字节数的方法
        self.assertEqual(self.utility.format_bytes(1024), '1.0 KB')
        self.assertEqual(self.utility.format_bytes(1048576), '1.0 MB')
        self.assertEqual(self.utility.format_bytes(0), '0 B')

    def test_is_valid_torrent_hash(self):
        # 测试验证种子 hash 是否有效的方法
        self.assertTrue(self.utility.is_valid_torrent_hash('1234abcd5678efgh'))
        self.assertFalse(self.utility.is_valid_torrent_hash('invalid_hash'))

    def tearDown(self):
        # 在每个测试后清理资源
        del self.utility
