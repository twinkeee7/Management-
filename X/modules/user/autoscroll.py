#MIT License

#Copyright (c) 2024 Japanese-X-Userbot

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

from pyrogram import Client, filters
from pyrogram.types import Message
from config import SUDO_USERS
from X.helpers.basic import edit_or_reply
from .help import *

the_regex = r"^r\/([^\s\/])+"

f = filters.chat([])


@Client.on_message(f)
async def auto_read(bot: Client, message: Message):
    await Client.read_history(message.chat.id)
    message.continue_propagation()


@Client.on_message(
    filters.command(["autoscroll"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def add_to_auto_read(bot: Client, message: Message):
    if message.chat.id in f:
        f.remove(message.chat.id)
        await message.edit("Autoscroll deactivated")
    else:
        f.add(message.chat.id)
        await message.edit("Autoscroll activated")


add_command_help(
    "•─╼⃝𖠁 ᴀᴜᴛᴏꜱᴄʀᴏʟʟ",
    [
        [
            ".autoscroll",
            "Sᴇɴᴅ .ᴀᴜᴛᴏꜱᴄʀᴏʟʟ ɪɴ ᴀɴʏ ᴄʜᴀᴛ ᴛᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʀᴇᴀᴅ ᴀʟʟ ꜱᴇɴᴛ ᴍᴇꜱꜱᴀɢᴇꜱ ᴜɴᴛɪʟ ʏᴏᴜ ᴄᴀʟʟ "
            "ᴀᴜᴛᴏꜱᴄʀᴏʟʟ ᴀɢᴀɪɴ. Tʜɪꜱ ɪꜱ ᴜꜱᴇғᴜʟ ɪғ ʏᴏᴜ ʜᴀᴠᴇ Tᴇʟᴇɢʀᴀᴍ ᴏᴘᴇɴ ᴏɴ ᴀɴᴏᴛʜᴇʀ ꜱᴄʀᴇᴇɴ.",
        ],
    ],
)
