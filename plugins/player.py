# Mʀ Nɪᴛʀɪᴄ // @MrNitric

import os
import aiofiles
import aiohttp
import ffmpeg
import requests
from os import path
from asyncio.queues import QueueEmpty
from typing import Callable
from pyrogram import Client, filters
from pyrogram.types import Message, Voice, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from modules.cache.admins import set
from modules.clientbot import clientbot, queues
from modules.clientbot.clientbot import client as USER
from modules.helpers.admins import get_administrators
from youtube_search import YoutubeSearch
from modules import converter
from modules.downloaders import youtube
from modules.config import DURATION_LIMIT, que, SUDO_USERS
from modules.cache.admins import admins as a
from modules.helpers.filters import command, other_filters
from modules.helpers.command import commandpro
from modules.helpers.decorators import errors, authorized_users_only
from modules.helpers.errors import DurationLimitError
from modules.helpers.gets import get_url, get_file_name
from PIL import Image, ImageFont, ImageDraw
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import InputAudioStream

# plus
chat_id = None
useer = "NaN"


def transcode(filename):
    ffmpeg.input(filename).output(
        "input.raw", format="s16le", acodec="pcm_s16le", ac=2, ar="48k"
    ).overwrite_output().run()
    os.remove(filename)


# Convert seconds to mm:ss
def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))


# Change image size
def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


async def generate_cover(title, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()
    image1 = Image.open("./background.png")
    image2 = Image.open("etc/foreground.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save("temp.png")
    img = Image.open("temp.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("etc/font.otf", 60)
    draw.text((40, 550), "Playing here...", (0, 0, 0), font=font)
    draw.text((40, 630), f"{title[:25]}...", (0, 0, 0), font=font)
    img.save("final.png")
    os.remove("temp.png")
    os.remove("background.png")


@Client.on_message(
    commandpro(["/play", "/yt", "/ytp", "play", "yt", "ytp", "@", "#"])
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def play(_, message: Message):
    global que
    global useer
    
    lel = await message.reply("**🔎**")

    administrators = await get_administrators(message.chat)
    chid = message.chat.id

    try:
        user = await USER.get_me()
    except:
        user.first_name = "Nitric_Player"
    usar = user
    wew = usar.id
    try:
        await _.get_chat_member(chid, wew)
    except:
        for administrator in administrators:
            if administrator == message.from_user.id:
                try:
                    invitelink = await _.export_chat_invite_link(chid)
                except:
                    await lel.edit(
                        "⚠️ **ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀᴅᴍɪɴ ғɪʀsᴛ ⚠️**")
                    return

                try:
                    await USER.join_chat(invitelink)
                    await USER.send_message(
                        message.chat.id, "**ʀᴇᴅ ʟɪɢʜᴛ ᴍᴜsɪᴄ ᴀssɪsᴛᴀɴᴛ ᴊᴏɪɴᴇᴅ 👍🏻 ɴᴏᴡ ᴘʟᴀʏ ʏᴏᴜʀ ᴍᴜsɪᴄ ғʀᴇᴇʟʏ** ❣")

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    await lel.edit(
                        f"⚠️ **ᴇʀʀᴏʀ ⚠️ ᴄʜᴇᴄᴋ ᴍᴀʏʙᴇ ʀᴇᴅ ʟɪɢʜᴛ ᴍᴜsɪᴄ ᴀssɪᴛᴀɴᴛ ɪs ʙᴀɴɴᴇᴅ ᴏʀ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴛʜɪs ᴄʜᴀᴛ <3 ᴏʀ ᴄᴏɴᴛᴀᴄᴛ - @MrNitric 👅**")
    try:
        await USER.get_chat(chid)
    except:
        await lel.edit(
            f"😒 **ʀᴇᴅ ʟɪɢʜᴛ ᴍᴜsɪᴄ ᴀssɪsᴛᴀɴᴛ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴛʜɪs ᴄʜᴀᴛ sᴏ sᴇɴᴅ /play ᴄᴏᴍᴍᴀɴᴅ ғɪʀsᴛ ᴛᴏ ᴊᴏɪɴ ᴀssɪsᴛᴀɴᴛ ʜᴇʀᴇ <3 ᴏʀ ᴄᴏɴᴛᴀᴄᴛ - @MrNitric 👅")
        return
    
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"🙃 **ʜᴇʏ ʏᴏᴜʀ sᴏɴɢ ᴅᴜʀᴀᴛɪᴏɴ ɪs {DURATION_LIMIT} ᴍɪɴᴜᴛᴇs, & ᴛʜɪs ɪs ɴᴏᴛ ᴀʟʟᴏᴡ ᴛᴏ ᴘʟᴀʏ** ️🤞"
            )

        file_name = get_file_name(audio)
        title = file_name
        thumb_name = "https://telegra.ph/file/e8726a1345addad530a3d.png"
        thumbnail = thumb_name
        duration = round(audio.duration / 60)
        views = "Locally added"

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="💡 ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/Sanki_BOTs"
                    ),
                    InlineKeyboardButton(text="ᴏᴡɴᴇʀ 🌸", url=f"https://t.me/thekingofbihar1235"),
                ]
            ]
        )

        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name))
            else file_name
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="💡 ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/Sanki_BOTs"
                        ),
                        InlineKeyboardButton(
                            text="ᴏᴡɴᴇʀ 🌸", url=f"https://t.me/thekingofbihar1235"
                        ),
                    ]
                ]
            )

        except Exception as e:
            title = "NaN"
            thumb_name = "https://telegra.ph/file/e8726a1345addad530a3d.png"
            duration = "NaN"
            views = "NaN"
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="💡 ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/Sanki_BOTs"
                        ),
                        InlineKeyboardButton(
                            text="ᴏᴡɴᴇʀ 🌸", url=f"https://t.me/thekingofbihar1235"
                        ),
                    ]
                ]
            )

        if (dur / 60) > DURATION_LIMIT:
            await lel.edit(
                f"**🙃 **ʜᴇʏ ʏᴏᴜʀ sᴏɴɢ ᴅᴜʀᴀᴛɪᴏɴ ɪs {DURATION_LIMIT} ᴍɪɴᴜᴛᴇs, & ᴛʜɪs ɪs ɴᴏᴛ ᴀʟʟᴏᴡ ᴛᴏ ᴘʟᴀʏ** ️🤞**"
            )
            return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(youtube.download(url))
    else:
        if len(message.command) < 2:
            return await lel.edit(
                "**🙃 **ʜᴇʏ ᴛʏᴘᴇ ᴛʜᴇ sᴏɴɢ ɴᴀᴍᴇ ʙᴀʙʏ...****"
            )
        await lel.edit("**🔍 **ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴛᴏ ʀᴇᴅ ʟɪɢʜᴛ sᴇʀᴠᴇʀ...****")
        query = message.text.split(None, 1)[1]
        # print(query)
        await lel.edit("🔍 **ᴘʟᴀʏɪɴɢ ᴠɪᴀ ʀᴇᴅ ʟɪɢʜᴛ sᴇʀᴠᴇʀ...**")
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            await lel.edit(
                "**⚠️ **sᴏʀʀʏ sᴏɴɢ ɴᴀᴍᴇ ᴡʀᴏɴɢ, ᴛʀʏ ᴡɪᴛʜ ʀɪɢʜᴛ ɴᴀᴍᴇ** 😾😒**"
            )
            print(str(e))
            return

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="💡 ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/Sanki_BOTs"
                    ),
                    InlineKeyboardButton(text="ᴏᴡɴᴇʀ 🌸", url=f"https://t.me/thekingofbihar1235"),
                ]
            ]
        )

        if (dur / 60) > DURATION_LIMIT:
            await lel.edit(
                f"**🙃 **ʜᴇʏ ʏᴏᴜʀ sᴏɴɢ ᴅᴜʀᴀᴛɪᴏɴ ɪs {DURATION_LIMIT} ᴍɪɴᴜᴛᴇs, & ᴛʜɪs ɪs ɴᴏᴛ ᴀʟʟᴏᴡ ᴛᴏ ᴘʟᴀʏ** ️🤞**"
            )
            return
        requested_by = message.from_user.first_name
        await generate_cover(title, thumbnail)
        file_path = await converter.convert(youtube.download(url))
 
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in clientbot.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(message.chat.id) in ACTV_CALLS:
        position = await queues.put(message.chat.id, file=file_path)
        await message.reply_photo(
            photo="final.png",
            caption=f"🏷 **ꜱᴏɴɢ ᴀᴅᴅᴇᴅ ᴛᴏ Qᴜᴇᴜᴇ »** `{position}`\n\n🏷 **ɴᴀᴍᴇ:** [{title[:80]}]({url})\n⏱ **ᴅᴜʀᴀᴛɪᴏɴ:** `{duration}`\n🎧 **ᴀᴅᴅᴇᴅ ʙʏ:** {message.from_user.mention}",
            reply_markup=keyboard,
        )
        os.remove("final.png")
        return await lel.delete()
    else:
        await clientbot.pytgcalls.join_group_call(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )

        await message.reply_photo(
            photo="final.png",
            caption=f"☑️ **ɴᴀᴍᴇ:** [{title[:80]}]({url})\n⏱ **ᴅᴜʀᴀᴛɪᴏɴ:** `{duration}`\n💡 **ꜱᴛᴀᴛᴜꜱ:** `ᴘʟᴀʏɪɴɢ`\n"
            + f"🎧 **ᴀᴅᴅᴇᴅ ʙʏ:** {message.from_user.mention}",
            reply_markup=keyboard,
        )
        os.remove("final.png")
        return await lel.delete()
    
    
@Client.on_message(commandpro(["/pause", "pause"]) & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    await clientbot.pytgcalls.pause_stream(message.chat.id)
    await message.reply_photo(
                             photo="https://telegra.ph/file/431b022f68a850aad802a.png", 
                             caption="**ʀᴇᴅ ʟɪɢʜᴛ ᴍᴜsɪᴄ sᴇʀᴠᴇʀ ɪs ᴘᴀᴜsᴇᴅ ❥︎**"
    )


@Client.on_message(commandpro(["/resume", "resume"]) & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    await clientbot.pytgcalls.resume_stream(message.chat.id)
    await message.reply_photo(
                             photo="https://telegra.ph/file/563589f6f4aa02dc3953f.png", 
                             caption="**ʀᴇᴅ ʟɪɢʜᴛ ᴍᴜsɪᴄ sᴇʀᴠᴇʀ ɪs ᴘʟᴀʏɪɴɢ ❥**"
    )



@Client.on_message(commandpro(["/skip", "/next", "skip", "next"]) & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in clientbot.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text("**ʀᴇᴅ ʟɪɢʜᴛ ᴍᴜsɪᴄ sᴇʀᴠᴇʀ ɪs ɴᴏᴛʜɪɴɢ ᴘʟᴀʏɪɴɢ ❥**")
    else:
        queues.task_done(chat_id)
        
        if queues.is_empty(chat_id):
            await clientbot.pytgcalls.leave_group_call(chat_id)
        else:
            await clientbot.pytgcalls.change_stream(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        clientbot.queues.get(chat_id)["file"],
                    ),
                ),
            )


    await message.reply_photo(
                             photo="https://telegra.ph/file/10cd011288efb2e36ff6a.png", 
                             caption=f'**ʀᴇᴅ ʟɪɢʜᴛ ᴍᴜsɪᴄ sᴇʀᴠᴇʀ ɪs sᴋɪᴘᴘᴇᴅ ᴛᴏ ɴᴇxᴛ ❥**'
   ) 


@Client.on_message(commandpro(["/end", "end", "/stop", "stop", "x"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    try:
        clientbot.queues.clear(message.chat.id)
    except QueueEmpty:
        pass

    await clientbot.pytgcalls.leave_group_call(message.chat.id)
    await message.reply_photo(
                             photo="https://telegra.ph/file/6ca8f7ef0bb3fd895afcf.png", 
                             caption="**ʀᴇᴅ ʟɪɢʜᴛ ᴍᴜsɪᴄ sᴇʀᴠᴇʀ ɪs ᴇɴᴅ ᴏʀ sᴛᴏᴘᴘᴇᴅ ❥**"
    )


@Client.on_message(commandpro(["reload", "refresh"]))
@errors
@authorized_users_only
async def admincache(client, message: Message):
    set(
        message.chat.id,
        (
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ),
    )

    await message.reply_photo(
                              photo="https://telegra.ph/file/d94c1e269b3d367a40e17.png",
                              caption="**ʀᴇᴅ ʟɪɢʜᴛ ᴍᴜsɪᴄ sᴇʀᴠᴇʀ ɪs ʀᴇʟᴏᴀᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ❥**"
    )
