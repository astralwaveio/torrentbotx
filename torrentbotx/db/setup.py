import sqlite3


def init_db():
    """初始化数据库"""
    db_file = 'data/torrentbotx.db'
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # 创建任务表
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        status TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')

    # 创建用户表
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        chat_id INTEGER
    )''')

    # 提交更改并关闭连接
    conn.commit()
    conn.close()


if __name__ == '__main__':
    init_db()
