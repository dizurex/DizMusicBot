
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters



HOME_TEXT = "<b>Hi, [{}](tg://user?id={})!\n\nI am Voice Chat Radio Player in\nChannels and Groups 24Γ7 NonStop.\n\nI can even Stream YouTube Live in VoiceChat!\n\nDeploy Your Own bot from [π here](https://github.com/dizurex/DizMusicBot).\n\nβ·Please Subscribe β€οΈ @dizurex</b>"
HELP = """**Only Admins Commands**:

**β·/radio:** Start Radio.
**β·/stop:** Stops Radio/LiveStream.
**β·/join:**  Join voice chat.
**β·/leave:**  Leave current voice chat
**β·/vc:**  Check which VC is joined.
**β·/mute:** Mute in Voice Chat.
**β·/unmute:** Unmute in Voice Chat.
**β·/pause:** Pause the Streaming.
**β·/resume:** Resume the paused Stream.
**β·/clean:** Clean RAW File's.
**β·/restart:** Restarts the Bot.
"""



@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('π» Listen here Radio', url='https://t.me/SHOTGVNgc?voicechat'),
    ],
    [
        InlineKeyboardButton('π₯ Group', url='https://t.me/SHOTGVNgc'),
        InlineKeyboardButton('Owner π’', url='https://t.me/dizurex'),
    ],
    [
        InlineKeyboardButton('π Helpful Commands π', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)



@Client.on_message(filters.command("help"))
async def show_help(client, message):
    buttons = [
        [
            InlineKeyboardButton('π» Listen here Radio', url='https://t.me/SHOTGVNgc?voicechat'),
        ],
        [
            InlineKeyboardButton('π₯ Group', url='https://t.me/SHOTGVNgc'),
            InlineKeyboardButton('Owner π’', url='https://t.me/dizurex'),
        ],
        [
            InlineKeyboardButton('π° How to Deploy π°', url='https://t.me/dizurex'),
        
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(
        HELP,
        reply_markup=reply_markup
        )
