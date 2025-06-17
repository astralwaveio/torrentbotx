from torrentbotx.bots.telegram.bot import start_bot
from torrentbotx.config.config import load_config
from torrentbotx.core.manager import CoreManager
from torrentbotx.db.setup import init_db
from torrentbotx.notifications.telegram_notifier import TelegramNotifier


def main():
    # 正确加载配置
    config = load_config()
    # 初始化数据库
    init_db()
    notifier = TelegramNotifier(
        bot_token=config.get("TG_BOT_TOKEN_MT"),
        chat_id=config.get("TG_ALLOWED_CHAT_IDS")
    )
    # 初始化核心管理器（注入 config 和 notifier）
    core_manager = CoreManager(config=config, notifier=notifier)
    # 启动核心管理器
    core_manager.start()
    # 启动 Telegram Bot（传入 CoreManager 实例）
    start_bot(config.get("TG_BOT_TOKEN_MT"), core_manager)


if __name__ == "__main__":
    main()
