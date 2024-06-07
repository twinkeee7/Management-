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
    filters.command(["osaka"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def castle(client, message):
    args = message.text.split(" ")[1:]
    castledata = [
  "https://graph.org/file/d1f9bf6ed087bd52305f2.jpg",
  "https://graph.org/file/9a9852c876b51267729eb.jpg",
  "https://graph.org/file/d00a1849c16271abcc787.jpg",
  "https://graph.org/file/8d84cc22b365cca74ea54.jpg",
  "https://graph.org/file/2c0cf62508006d18b5c11.jpg",
  "https://graph.org/file/9fd072388b0b4ca9833ce.jpg",
  "https://graph.org/file/53cdcda9ff5af53a993b1.jpg",
  "https://graph.org/file/d1f9bf6ed087bd52305f2.jpg",
    ]
    castle_url = random.choice(castledata)
    await message.reply_photo(castle_url)

add_command_help(
    "•─╼⃝𖠁 Osᴀᴋᴀ",
    [
       ["osaka", "Gɪᴠᴇ random Osᴀᴋᴀ pic."],
        ],
)
