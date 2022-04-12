import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
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
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/c6e1041c6c9a12913f57a.png",
        caption=f"""**Hᴇʏ Hᴏᴛᴛɪᴇ Sʜᴏᴛᴛɪᴇ, 
        I Aᴍ A Mᴜsɪᴄ Sᴇʀᴠᴇʀ Fᴏʀ Yᴏᴜʀ Tᴇʟᴇɢʀᴀᴍ Vᴏɪᴄᴇ Cʜᴀᴛ & Cʜᴀɴɴᴇʟs 😉🌸 Usᴇ Mᴇ Hᴀʀᴅʟʏ & Eɴᴊᴏʏ Mᴜsɪᴄ Wɪᴛʜ Sᴜᴘᴇʀ Dᴜᴘᴇʀ Qᴜᴀʟɪᴛʏ 😈❣️
Dᴇᴠᴇʟᴏᴘᴇᴅ Bʏ : [𝐍 𝐢 𝐭 𝐫 𝐢 𝐜 𓆩👅𓆪](https://t.me/MrNitric).**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌸 ᴏᴡɴᴇʀ 🌸", url="https://t.me/thekingofbihar1235")
                  ],[
                    InlineKeyboardButton(
                        "💡 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/Sanki_BOTs"
                    ),
                    InlineKeyboardButton(
                        "ʀᴇᴘᴏ 🎈", url="https://github.com/NitricXd/RedLightMusicBot"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "⁉️ ʜᴇʟᴘ ‼️", url="https://telegra.ph/R%E1%B4%87%E1%B4%85-L%C9%AA%C9%A2%CA%9C%E1%B4%9B-M%E1%B4%9Cs%C9%AA%E1%B4%84-S%E1%B4%87%CA%80%E1%B4%A0%E1%B4%87%CA%80-04-12"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "aditya"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/92b951ae9a3e4f19d7f64.png",
        caption=f"""ʀᴇᴅ ʟɪɢʜᴛ sᴇʀᴠᴇʀ ɪs ᴀʟɪᴠᴇ ʙᴀʙʏ 😈""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💡 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/Sanki_BOTs")
                ]
            ]
        )
   )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fda1150381f0388334632.png",
        caption=f"""ʀᴇᴅ ʟɪɢʜᴛ sᴇʀᴠᴇʀ ʀᴇᴘᴏ ᴍᴇɴᴜ 👅""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❥︎ ᴄʟɪᴄᴋ ᴍᴇ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ ❥︎", url=f"https://t.me/MrNitric")
                ]
            ]
        ),
    )
