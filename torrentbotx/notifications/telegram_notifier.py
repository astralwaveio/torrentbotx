import logging

from telegram import Bot
from telegram.error import TelegramError

from torrentbotx.notifications.notifier import Notifier

logger = logging.getLogger("notifications")


class TelegramNotifier(Notifier):
    def __init__(self, bot_token: str, chat_id: str):
        self.bot = Bot(token=bot_token)
        self.chat_id = chat_id

    def send_message(self, message: str):
        try:
            self.bot.send_message(chat_id=self.chat_id, text=message)
            logger.info(f"成功发送消息到 {self.chat_id}")
        except TelegramError as e:
            logger.error(f"发送 Telegram 消息失败: {e}")
