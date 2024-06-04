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

import random
from pyrogram import Client, filters
from config import SUDO_USERS
from .help import * 

hl = "."

@Client.on_message(
    filters.command(["allerton"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def castle(client, message):
    args = message.text.split(" ")[1:]
    castledata = [
  "https://graph.org/file/539f1f6c54cacd1d6dd16.jpg",
  "https://graph.org/file/affcff3cb2cf03530626e.jpg",
  "https://graph.org/file/d54e7d64ca5ec1f3ca452.jpg",
  "https://graph.org/file/82d5624b919e125d1da1a.jpg",
  "https://graph.org/file/6c584b958c776e265734a.jpg",
  "https://graph.org/file/3663ccfe7407ca404495a.jpg",
  "https://graph.org/file/affcff3cb2cf03530626e.jpg",
  "https://graph.org/file/d54e7d64ca5ec1f3ca452.jpg",
    ]
    castle_url = random.choice(castledata)
    await message.reply_photo(castle_url)

add_command_help(
    "•─╼⃝𖠁 Aʟʟᴇʀᴛᴏɴ Cᴀsᴛʟᴇ",
    [
       ["allerton", "Gɪᴠᴇ random Aʟʟᴇʀᴛᴏɴ Cᴀsᴛʟᴇ pic."],
        ],
)
