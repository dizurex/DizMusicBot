
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters



HOME_TEXT = "<b>Hi, [{}](tg://user?id={})!\n\nI am Voice Chat Radio Player in\nChannels and Groups 24×7 NonStop.\n\nI can even Stream YouTube Live in VoiceChat!\n\nDeploy Your Own bot from [👉 here](https://github.com/dizurex/DizMusicBot).\n\n▷Please Subscribe ❤️ @dizurex</b>"
HELP = """**Only Admins Commands**:

**▷/radio:** Start Radio.
**▷/stop:** Stops Radio/LiveStream.
**▷/join:**  Join voice chat.
**▷/leave:**  Leave current voice chat
**▷/vc:**  Check which VC is joined.
**▷/mute:** Mute in Voice Chat.
**▷/unmute:** Unmute in Voice Chat.
**▷/pause:** Pause the Streaming.
**▷/resume:** Resume the paused Stream.
**▷/clean:** Clean RAW File's.
**▷/restart:** Restarts the Bot.
"""



@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('📻 Listen here Radio', url='https://t.me/SHOTGVNgc?voicechat'),
    ],
    [
        InlineKeyboardButton('👥 Group', url='https://t.me/SHOTGVNgc'),
        InlineKeyboardButton('Owner 📢', url='https://t.me/dizurex'),
    ],
    [
        InlineKeyboardButton('🆘 Helpful Commands 🆘', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)



@Client.on_message(filters.command("help"))
async def show_help(client, message):
    buttons = [
        [
            InlineKeyboardButton('📻 Listen here Radio', url='https://t.me/SHOTGVNgc?voicechat'),
        ],
        [
            InlineKeyboardButton('👥 Group', url='https://t.me/SHOTGVNgc'),
            InlineKeyboardButton('Owner 📢', url='https://t.me/dizurex'),
        ],
        [
            InlineKeyboardButton('🔰 How to Deploy 🔰', url='https://t.me/dizurex'),
        
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(
        HELP,
        reply_markup=reply_markup
        )
