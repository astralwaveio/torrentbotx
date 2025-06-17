import unittest
from unittest.mock import patch, MagicMock
from telegram import Update, Bot
from telegram.ext import CommandHandler, CallbackContext
from torrentbotx.bots.telegram import TelegramBot

class TestTelegramBot(unittest.TestCase):

    @patch.object(Bot, 'send_message')
    def test_start_command(self, mock_send_message):
        # 模拟 Telegram Bot 的 /start 命令
        bot = MagicMock()
        update = MagicMock()
        update.message.text = "/start"
        update.message.chat.id = 1234
        context = MagicMock()

        telegram_bot = TelegramBot(bot)
        telegram_bot.start_command(update, context)

        mock_send_message.assert_called_once_with(chat_id=1234, text="欢迎使用 M-Team 与 qBittorrent 管理助手！")

    @patch.object(Bot, 'send_message')
    def test_help_command(self, mock_send_message):
        # 测试帮助命令
        bot = MagicMock()
        update = MagicMock()
        update.message.text = "/help"
        update.message.chat.id = 1234
        context = MagicMock()

        telegram_bot = TelegramBot(bot)
        telegram_bot.help_command(update, context)

        mock_send_message.assert_called_once_with(chat_id=1234, text="💡 M-Team 与 qBittorrent 管理助手 - 帮助信息")

    def tearDown(self):
        # 清理资源
        pass
