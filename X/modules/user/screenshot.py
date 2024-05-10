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

# Credits: Athfan Khaleel
# Copyright (C) https://github.com/athphane/userbot
#REMAKE BY NOBITA XD AND TRYTOLIVEALONE 



import asyncio

from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message

from X.helpers.basic import edit_or_reply

from .help import *


@Client.on_message(
    filters.command(["ss"], ".") & filters.private & filters.me
)
async def screenshot(bot: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        bot.invoke(
            functions.messages.SendScreenshotNotification(
                peer=await Client.resolve_peer(message.chat.id),
                reply_to_msg_id=0,
                random_id=Client.rnd_id(),
            )
        ),
    )


add_command_help(
    "•─╼⃝𖠁 ꜱᴄʀᴇᴇɴꜱʜᴏᴛ",
    [
        [
            ".ss",
            "Sᴇɴᴅ ᴀ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ ᴀ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ (ɴᴏᴛ ꜱᴇᴄʀᴇᴛ) ᴛᴏ ᴀɴɴᴏʏ ᴏʀ ᴛʀᴏʟʟ ʏᴏᴜʀ ғʀɪᴇɴᴅꜱ.",
        ],
    ],
)
