import asyncio

from telegram.ext import Application

from torrentbotx.bots.telegram.updater import setup_application
from torrentbotx.core.manager import CoreManager
from torrentbotx.utils.logger import get_logger

logger = get_logger("telegram_bot")


def start_bot(bot_token: str, core_manager: CoreManager):
    logger.info("🎯 启动 Telegram Bot...")
    try:
        asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    application = Application.builder().token(bot_token).build()
    application.bot_data["core_manager"] = core_manager

    setup_application(application, bot_token)

    logger.info("🔄 机器人正在运行...")
    application.run_polling()
