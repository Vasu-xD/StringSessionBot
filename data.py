from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("Generate Session", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🔙 Back", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton("Commands ❔", callback_data="help"),
            InlineKeyboardButton("🖥 About", callback_data="about")
        ],
        [InlineKeyboardButton("🎉 Awesome Bots", url="https://t.me/VasuBots")],
    ]

    START = """
**Hey {}!
Welcome to {}, A Simple Telethon And Pyrogram Session Generator Bot.

You can use me to generate pyrogram and telethon string session for a user account or bot. Use below buttons to learn more !

☘ By @VasuBots**
    """

    HELP = """
✨ **Available Commands** ✨

**/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/restart - Cancel the process**
"""

    ABOUT = """
**Telegram Bot to generate Pyrogram and Telethon string session By @VasuBots**

💡 Framework : [Pyrogram](https://docs.pyrogram.org)

🏳️‍🌈 Language : [Python](https://www.python.org)

**🧑🏻‍💻 Developer : @VasuXD**
    """
