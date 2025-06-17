# tasks/tasks.py
from datetime import datetime

from ..notifications.telegram_notifier import TelegramNotifier
from ..notifications.notifier import Notifier
from ..utils import logger

log = logger.get_logger()


def example_task():
    """
    示例任务，用于演示如何在任务执行后发送通知
    """
    # 任务执行的逻辑
    # 这里可以是任何你需要执行的代码

    # 任务完成后，发送通知
    notifier: Notifier = TelegramNotifier(bot_token="YOUR_BOT_TOKEN", chat_id="YOUR_CHAT_ID")
    notifier.send_message("任务执行完成！")
    log.info(f"示例任务执行中，当前时间: {datetime.now()}")
    # 在这里放置具体任务逻辑，例如清理过期的下载任务或抓取PT站点的种子


def task_with_error():
    """
    任务执行过程中发生错误时发送通知
    """
    try:
        # 模拟任务代码
        raise ValueError("任务发生了一个错误")
    except Exception as e:
        # 任务发生错误后，发送通知
        notifier: Notifier = TelegramNotifier(bot_token="YOUR_BOT_TOKEN", chat_id="YOUR_CHAT_ID")
        notifier.send_message(f"任务失败: {str(e)}")
