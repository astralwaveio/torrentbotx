from torrentbotx.db.models import create_tables


def init_db() -> None:
    """初始化数据库表结构."""
    create_tables()


if __name__ == '__main__':
    init_db()
