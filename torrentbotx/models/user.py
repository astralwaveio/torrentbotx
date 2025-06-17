from typing import List


class User:
    def __init__(self, user_id: str, username: str, permissions: List[str]):
        """
        用户模型，用于存储用户的信息
        :param user_id: 用户ID
        :param username: 用户名
        :param permissions: 用户的权限列表（如添加种子、查看任务等）
        """
        self.user_id = user_id
        self.username = username
        self.permissions = permissions

    def to_dict(self) -> dict:
        """
        将用户模型转换为字典
        :return: 字典形式的用户数据
        """
        return {
            "user_id": self.user_id,
            "username": self.username,
            "permissions": self.permissions
        }

    @staticmethod
    def from_dict(data: dict) -> 'User':
        """
        从字典数据创建用户模型
        :param data: 字典数据
        :return: 创建的 User 实例
        """
        return User(
            user_id=data.get("user_id"),
            username=data.get("username"),
            permissions=data.get("permissions", [])
        )
