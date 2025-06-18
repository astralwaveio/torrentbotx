import sqlite3

from torrentbotx.db.connection import create_connection


def insert_torrent(name, t_hash, category, state, added_on, progress, ratio):
    """插入一个新的种子记录"""
    conn = create_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO torrents (name, hash, category, state, added_on, progress, ratio)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (name, t_hash, category, state, added_on, progress, ratio),
        )
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"插入种子数据时出错: {e}")


def get_torrent_by_hash(t_hash):
    """根据hash获取种子信息"""
    conn = create_connection()
    if conn is None:
        return None
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM torrents WHERE hash = ?', (t_hash,))
        row = cursor.fetchone()
        conn.close()
        return row
    except sqlite3.Error as e:
        print(f"查询种子数据时出错: {e}")
        return None


def update_task_status(task_id, status):
    """更新任务的状态"""
    conn = create_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE tasks SET status = ? WHERE id = ?', (status, task_id)
        )
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"更新任务状态时出错: {e}")
