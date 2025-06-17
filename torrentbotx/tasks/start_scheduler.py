from torrentbotx.tasks.scheduler import TaskScheduler
from torrentbotx.tasks.tasks import example_task


def start_all_tasks():
    """
    启动所有任务
    """
    scheduler = TaskScheduler()

    # 启动调度器
    scheduler.start()

    # 添加任务到调度器
    scheduler.add_task(example_task, 'interval', minutes=10)  # 每10分钟执行一次示例任务
    scheduler.add_task(example_task, 'cron', hour=8, minute=0)  # 每天早上8点执行一次示例任务

    # 列出当前的所有任务
    scheduler.list_jobs()

    return scheduler
