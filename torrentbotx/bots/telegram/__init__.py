"""简化版 Telegram Bot，仅用于单元测试."""

from telegram import Bot


class TelegramBot:
    """Very small Telegram bot wrapper used in tests."""

    def __init__(self, bot) -> None:
        self.bot = bot

    def start_command(self, update, context) -> None:
        chat_id = update.message.chat.id
        Bot.send_message(self.bot, chat_id=chat_id, text="欢迎使用 M-Team 与 qBittorrent 管理助手！")

    def help_command(self, update, context) -> None:
        chat_id = update.message.chat.id
        Bot.send_message(self.bot, chat_id=chat_id, text="💡 M-Team 与 qBittorrent 管理助手 - 帮助信息")


__all__ = ["TelegramBot"]

