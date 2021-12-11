import asyncio
from time import time
from datetime import datetime
from Music import BOT_USERNAME
from Music.config import UPDATES_CHANNEL, ZAID_SUPPORT
from Music.MusicUtilities.helpers.filters import command
from Music.MusicUtilities.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   


    
    
@Client.on_message(commandpro(["/start"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/e3c1e773a8e0fd11f53ed.jpg",
        caption=f"""𝐍𝐎𝐈𝐍𝐎𝐈 𝐌𝐔𝐒𝐈𝐂 🎶 𝗦𝗨𝗣𝗘𝗥𝗙𝗔𝗦𝗧 𝗠𝗨𝗦𝗜𝗖 𝗕𝗢𝗧""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴊᴏɪɴ ʜᴇʀᴇ 💞", url=f"https://t.me/CFC_BOT_SUPPORT")
                ]
            ]
        ),
    )


@Client.on_message(command(["noinoi", "bazi"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/e3c1e773a8e0fd11f53ed.jpg",
        caption=f"""𝐍𝐎𝐈𝐍𝐎𝐈 𝐌𝐔𝐒𝐈𝐂 🎶 𝗦𝗨𝗣𝗘𝗥𝗙𝗔𝗦𝗧 𝗠𝗨𝗦𝗜𝗖 𝗕𝗢𝗧✨ \n\n ✨ FEATURS OF NOINOI \n ✨ MUSIC PLAYER \n ✨ GROUP MANAGER \n ✨ MENTION BOT \n ✨ COMING LOGO...""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " BAZIGAR ‼", url=f"https://t.me/bazigarYt")
                ]
            ]
        ),
    )
