from typing import Optional


class Torrent:
    def __init__(self, torrent_id: str, name: str, size: int, status: str, category: Optional[str] = None):
        """
        种子模型，用于管理种子的信息
        :param torrent_id: 种子ID
        :param name: 种子名称
        :param size: 种子文件大小
        :param status: 种子状态（如下载中、完成等）
        :param category: 种子的分类（如电影、音乐等）
        """
        self.torrent_id = torrent_id
        self.name = name
        self.size = size
        self.status = status
        self.category = category

    def to_dict(self) -> dict:
        """
        将模型转换为字典
        :return: 字典形式的种子数据
        """
        return {
            "torrent_id": self.torrent_id,
            "name": self.name,
            "size": self.size,
            "status": self.status,
            "category": self.category
        }

    @staticmethod
    def from_dict(data: dict) -> 'Torrent':
        """
        从字典数据创建种子模型
        :param data: 字典数据
        :return: 创建的 Torrent 实例
        """
        return Torrent(
            torrent_id=data.get("torrent_id"),
            name=data.get("name"),
            size=data.get("size"),
            status=data.get("status"),
            category=data.get("category")
        )
