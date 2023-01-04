
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import pyrogram
from Config import Config
from datetime import datetime
from telethon import Button


app = Client(
    "MentionAll",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
)

@app.on_message(filters.new_chat_members, group=1)
async def hg(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(Config.BOT_ID):
            await msg.reply(
                f'''`Salam` {msg.from_user.mention} `məni` {msg.chat.title} `qrupuna əlavə etdiyiniz üçün təşəkkürlər🥰`**''')

        elif str(new_user.id) == str(Config.OWNER_ID):
            await msg.reply('İndicə Sahibim qrupumuza qoşuldu😍\nXoş gəldin aramıza Sahibim❤️')

            buttons = [[InlineKeyboardButton("➕ Qrupa Əlavə Et ➕",url="http://t.me/Rahid_Tag_Bot?startgroup=a"),
                    InlineKeyboardButton("🙇🏻 Sahib", url="https://t.me/Rahid_2003"),
                    InlineKeyboardButton("🔮 Rəsmi", url="https://t.me/Rahid_44")]]

