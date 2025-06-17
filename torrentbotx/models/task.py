from typing import Optional


class Task:
    def __init__(self, task_id: str, name: str, status: str, priority: int, torrent_id: Optional[str] = None):
        """
        任务模型，用于管理任务的信息
        :param task_id: 任务ID
        :param name: 任务名称
        :param status: 任务状态（如待处理、进行中、已完成）
        :param priority: 任务优先级（0表示最高优先级）
        :param torrent_id: 任务关联的种子ID（如果有）
        """
        self.task_id = task_id
        self.name = name
        self.status = status
        self.priority = priority
        self.torrent_id = torrent_id

    def to_dict(self) -> dict:
        """
        将任务模型转换为字典
        :return: 字典形式的任务数据
        """
        return {
            "task_id": self.task_id,
            "name": self.name,
            "status": self.status,
            "priority": self.priority,
            "torrent_id": self.torrent_id
        }

    @staticmethod
    def from_dict(data: dict) -> 'Task':
        """
        从字典数据创建任务模型
        :param data: 字典数据
        :return: 创建的 Task 实例
        """
        return Task(
            task_id=data.get("task_id"),
            name=data.get("name"),
            status=data.get("status"),
            priority=data.get("priority"),
            torrent_id=data.get("torrent_id")
        )
