from telegram import Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from torrentbotx.bots.telegram.handler import start, help_command, add_task, qbtasks, cancel
from torrentbotx.utils.logger import get_logger

logger = get_logger("telegram_updater")


async def setup_application(application: Application, bot_token: str):
    """
    设置机器人应用，注册命令和消息处理器
    """
    bot = Bot(bot_token)
    application.bot = bot

    # 注册命令处理器
    logger.info("🔄 正在设置 Telegram 机器人应用...")
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("add", add_task))
    application.add_handler(CommandHandler("qbtasks", qbtasks))
    application.add_handler(CommandHandler("cancel", cancel))

    # 其他消息处理
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_unknown))


async def handle_unknown(update, context):
    """
    处理用户发送的未知消息
    """
    await update.message.reply_text("⚠️ 该命令未定义或无法识别，请使用 /help 获取更多帮助。")
