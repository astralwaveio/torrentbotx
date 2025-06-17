import sqlite3

from torrentbotx.config.config import load_config

config = load_config()

DB_PATH = config.get('DB_PATH', 'data/torrentbotx.db')


def create_connection():
    """创建和返回数据库连接"""
    try:
        conn = sqlite3.connect(DB_PATH)
        # 使得可以通过列名访问数据
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"SQLite 错误: {e}")
        return None
