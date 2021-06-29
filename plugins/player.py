
import os
from config import Config
from pyrogram import Client, filters, emoji
from pyrogram.methods.messages.download_media import DEFAULT_DOWNLOAD_DIR
from pyrogram.types import Message
from utils import mp, RADIO
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Python_ARQ import ARQ
from youtube_search import YoutubeSearch
from pyrogram import Client
from aiohttp import ClientSession
import re

LOG_GROUP=Config.LOG_GROUP

DURATION_LIMIT = Config.DURATION_LIMIT
ARQ_API=Config.ARQ_API
session = ClientSession()
arq = ARQ("https://thearq.tech",ARQ_API,session)
playlist=Config.playlist

ADMINS=Config.ADMINS
CHAT=Config.CHAT
LOG_GROUP=Config.LOG_GROUP
playlist=Config.playlist


@Client.on_message(filters.command("join") & filters.user(ADMINS))
async def join_group_call(client, m: Message):
    group_call = mp.group_call
    if group_call.is_connected:
        await m.reply_text(f"{emoji.ROBOT} Already joined voice chat")
        return
    await mp.start_call()
    chat = await client.get_chat(CHAT)
    await m.reply_text(f"Succesfully Joined Voice Chat in {chat.title}")


@Client.on_message(filters.command("leave") & filters.user(ADMINS))
async def leave_voice_chat(_, m: Message):
    group_call = mp.group_call
    if not group_call.is_connected:
        await m.reply_text("Not joined any Voicechat yet.")
        return
    playlist.clear()
    group_call.input_filename = ''
    await group_call.stop()
    await m.reply_text("Left the VoiceChat")


@Client.on_message(filters.command("vc") & filters.user(ADMINS))
async def list_voice_chat(client, m: Message):
    group_call = mp.group_call
    if group_call.is_connected:
        chat_id = int("-100" + str(group_call.full_chat.id))
        chat = await client.get_chat(chat_id)
        await m.reply_text(
            f"{emoji.MUSICAL_NOTES} **Currently in the voice chat**:\n"
            f"- **{chat.title}**"
        )
    else:
        await m.reply_text(emoji.NO_ENTRY
                                   + "Didn't join any voice chat yet")


@Client.on_message(filters.command("pause") & filters.user(ADMINS))
async def pause_playing(_, m: Message):
    group_call = mp.group_call
    if not group_call.is_connected:
        await m.reply_text("Nothing playing to pause.")
        return
    mp.group_call.pause_playout()
    await m.reply_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} Paused",
                               quote=False)



@Client.on_message(filters.command("resume") & filters.user(ADMINS))
async def resume_playing(_, m: Message):
    if not mp.group_call.is_connected:
        await m.reply_text("Nothing paused to resume.")
        return
    mp.group_call.resume_playout()
    await m.reply_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} Resumed",
                               quote=False)

@Client.on_message(filters.command("clean") & filters.user(ADMINS))
async def clean_raw_pcm(client, m: Message):
    download_dir = os.path.join(client.workdir, DEFAULT_DOWNLOAD_DIR)
    all_fn: list[str] = os.listdir(download_dir)
    for track in playlist[:2]:
        track_fn = f"{track[1]}.raw"
        if track_fn in all_fn:
            all_fn.remove(track_fn)
    count = 0
    if all_fn:
        for fn in all_fn:
            if fn.endswith(".raw"):
                count += 1
                os.remove(os.path.join(download_dir, fn))
    await m.reply_text(f"{emoji.WASTEBASKET} Cleaned {count} files")


@Client.on_message(filters.command("mute") & filters.user(ADMINS))
async def mute(_, m: Message):
    group_call = mp.group_call
    if not group_call.is_connected:
        await m.reply_text("Nothing playing to mute.")
        return
    group_call.set_is_mute(True)
    await m.reply_text(f"{emoji.MUTED_SPEAKER} Muted")


@Client.on_message(filters.command("unmute") & filters.user(ADMINS))
async def unmute(_, m: Message):
    group_call = mp.group_call
    if not group_call.is_connected:
        await m.reply_text("Nothing playing to mute.")
        return
    group_call.set_is_mute(False)
    await m.reply_text(f"{emoji.SPEAKER_MEDIUM_VOLUME} Unmuted")


admincmds=["join", "unmute", "mute", "leave", "clean", "vc", "pause", "resume", "radio", "stopradio", "restart"]

@Client.on_message(filters.command(admincmds) & ~filters.user(ADMINS))
async def notforu(_, m: Message):
    await m.reply("Who the hell you are")
