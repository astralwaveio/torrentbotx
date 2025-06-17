from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from torrentbotx.utils.logger import get_logger

logger = get_logger()


class TaskScheduler:
    def __init__(self):
        """
        初始化任务调度器
        """
        self.scheduler = BackgroundScheduler()
        self.scheduler.add_listener(self._job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
        logger.info("任务调度器初始化完成。")

    def start(self):
        """
        启动调度器
        """
        try:
            self.scheduler.start()
            logger.info("任务调度器已启动。")
        except Exception as e:
            logger.error(f"启动任务调度器失败: {e}")

    def stop(self):
        """
        停止调度器
        """
        try:
            self.scheduler.shutdown()
            logger.info("任务调度器已停止。")
        except Exception as e:
            logger.error(f"停止任务调度器失败: {e}")

    def add_task(self, func, trigger, **kwargs):
        """
        添加定时任务
        :param func: 任务函数
        :param trigger: 触发器（例如: 'interval', 'cron', 'date'）
        :param kwargs: 任务的触发参数（例如 interval=5, hours=1 等）
        """
        try:
            self.scheduler.add_job(func, trigger, **kwargs)
            logger.info(f"任务 '{func.__name__}' 已添加。")
        except Exception as e:
            logger.error(f"添加任务 '{func.__name__}' 失败: {e}")

    def remove_task(self, job_id):
        """
        移除任务
        :param job_id: 任务ID
        """
        try:
            self.scheduler.remove_job(job_id)
            logger.info(f"任务 '{job_id}' 已移除。")
        except Exception as e:
            logger.error(f"移除任务 '{job_id}' 失败: {e}")

    def list_jobs(self):
        """
        列出当前所有任务
        """
        jobs = self.scheduler.get_jobs()
        logger.info(f"当前任务数量: {len(jobs)}")
        for job in jobs:
            logger.info(f"任务: {job.id} | 下次执行: {job.next_run_time}")

    @staticmethod
    def _job_listener(event):
        """
        监听任务执行结果
        """
        if event.exception:
            logger.error(f"任务 '{event.job_id}' 执行失败！")
        else:
            logger.info(f"任务 '{event.job_id}' 执行成功。")
