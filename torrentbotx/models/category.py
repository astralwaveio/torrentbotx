class Category:
    def __init__(self, category_id: str, name: str):
        """
        分类模型，用于管理任务分类
        :param category_id: 分类ID
        :param name: 分类名称
        """
        self.category_id = category_id
        self.name = name

    def to_dict(self) -> dict:
        """
        将分类模型转换为字典
        :return: 字典形式的分类数据
        """
        return {
            "category_id": self.category_id,
            "name": self.name
        }

    @staticmethod
    def from_dict(data: dict) -> 'Category':
        """
        从字典数据创建分类模型
        :param data: 字典数据
        :return: 创建的 Category 实例
        """
        return Category(
            category_id=data.get("category_id"),
            name=data.get("name")
        )
