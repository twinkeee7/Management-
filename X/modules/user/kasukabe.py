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
    filters.command(["kasukabe"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def hinata(client, message):
    args = message.text.split(" ")[1:]
    hinatadata = [
  "https://graph.org/file/121d78924750d539de018.jpg",
  "https://graph.org/file/aaa4b76dc13e37ca23783.jpg",
  "https://graph.org/file/227228607397aefe1f0da.jpg",
  "https://graph.org/file/cb755e82d3d4fa74e5e8a.jpg",
  "https://graph.org/file/cc314e6499f0ae72e3a0b.jpg",
  "https://graph.org/file/5e9722fdf1cc21f7847a8.jpg",
  "https://graph.org/file/aaa4b76dc13e37ca23783.jpg",
  "https://graph.org/file/121d78924750d539de018.jpg",
    ]
    hinata_url = random.choice(hinatadata)
    await message.reply_photo(hinata_url)

add_command_help(
    "•─╼⃝𖠁 Kᴀsᴜᴋᴀʙᴇ",
    [
       ["kasukabe", "Gɪᴠᴇ random Kᴀsᴜᴋᴀʙᴇ pic."],
        ],
)
