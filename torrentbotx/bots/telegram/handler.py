from telegram import Update
from telegram.ext import ContextTypes

from torrentbotx.utils.logger import get_logger

logger = get_logger("telegram_handler")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    /start 命令处理，向用户发送欢迎消息
    """
    user = update.effective_user
    logger.info(f"欢迎用户: {user.id if user else 'Unknown'}")
    await update.message.reply_text(f"您好，{user.mention_html()}！欢迎使用我们的自动化下载工具。", parse_mode="HTML")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    /help 命令处理，向用户展示帮助信息
    """
    help_text = (
        "<b>💡 机器人命令帮助：</b>\n\n"
        "/start - 启动并显示欢迎信息。\n"
        "/help - 显示帮助信息。\n"
        "/add [M-Team ID] - 添加 M-Team ID 对应的种子到下载队列。\n"
        "/qbtasks - 显示当前下载任务。\n"
        "/cancel - 取消当前操作。\n"
    )
    await update.message.reply_html(help_text)


async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    /add [M-Team ID] 命令处理，添加下载任务
    """
    if not context.args:
        await update.message.reply_text("⚠️ 请输入 M-Team ID，例如: /add 12345")
        return

    mt_id = context.args[0]
    logger.info(f"用户请求添加 M-Team ID {mt_id} 的任务。")
    core_manager = context.bot_data["core_manager"]

    # 执行下载任务
    success = core_manager.execute_task("download", {"torrent_id": mt_id})
    if success:
        await update.message.reply_text(f"✅ 已成功添加种子 ID {mt_id} 到下载队列。")
    else:
        await update.message.reply_text(f"❌ 无法添加种子 ID {mt_id}，请稍后再试。")


async def qbtasks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    /qbtasks 命令处理，查看当前的下载任务状态
    """
    logger.info("用户请求查看当前下载任务。")
    core_manager = context.bot_data["core_manager"]

    # 获取当前任务列表
    tasks = core_manager.execute_task("get_current_tasks", {})
    if tasks:
        tasks_text = "\n".join([f"📝 {task['name']} - 状态: {task['status']}" for task in tasks])
        await update.message.reply_text(f"🔄 当前下载任务：\n{tasks_text}")
    else:
        await update.message.reply_text("❌ 当前没有任何下载任务。")


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    /cancel 命令处理，取消当前任务
    """
    logger.info(f"用户请求取消当前任务。")
    core_manager = context.bot_data["core_manager"]

    # 执行取消任务
    success = core_manager.execute_task("cancel_current_task", {})
    if success:
        await update.message.reply_text("✅ 已成功取消当前任务。")
    else:
        await update.message.reply_text("❌ 无法取消任务，可能没有正在进行的任务。")
