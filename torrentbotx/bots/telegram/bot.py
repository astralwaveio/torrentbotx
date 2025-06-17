from telegram.ext import Application

from torrentbotx.bots.telegram.updater import setup_application
from torrentbotx.core.manager import CoreManager
# 初始化日志
from torrentbotx.utils.logger import get_logger

logger = get_logger("telegram_bot")


def start_bot(bot_token: str, core_manager: CoreManager):
    """
    启动 Telegram Bot
    """
    logger.info("🎯 启动 Telegram Bot...")
    application = Application.builder().token(bot_token).build()

    # 将核心管理器传递给每个 handler
    application.bot_data["core_manager"] = core_manager

    # 设置处理器
    setup_application(application, bot_token)

    # 启动机器人
    logger.info("🔄 机器人正在运行...")
    application.run_polling()
