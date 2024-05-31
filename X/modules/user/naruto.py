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
    filters.command(["naruto"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def naruto(client, message):
    args = message.text.split(" ")[1:]
    narutodata = [
  "https://graph.org/file/8fce7cc2772cc1019bae7.jpg",
  "https://graph.org/file/2d2c05e2aff362cbf53b5.jpg",
  "https://graph.org/file/462819a7ec630262e707d.jpg",
  "https://graph.org/file/10df5c17f1b54de0e0b3a.jpg",
  "https://graph.org/file/556ab5451f992560bd443.jpg",
  "https://graph.org/file/f8790f64533dedddd6aeb.jpg",
  "https://graph.org/file/0dbd7f3b7683ce2d9a8cf.jpg",
  "https://graph.org/file/b6c2f34cd985a2d65b08a.jpg",
    ]
    naruto_url = random.choice(narutodata)
    await message.reply_photo(naruto_url)

add_command_help(
    "•─╼⃝𖠁 Nᴀʀᴜᴛᴏ",
    [
       ["naruto", "Gɪᴠᴇ random Nᴀʀᴜᴛᴏ pic."],
        ],
)
