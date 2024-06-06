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
    filters.command(["blossom"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def castle(client, message):
    args = message.text.split(" ")[1:]
    castledata = [
  "https://graph.org/file/4ba6fb292fedd6e071996.jpg",
  "https://graph.org/file/dbea429cbd1644a800f62.jpg",
  "https://graph.org/file/b0b8a357cb7dadfb7e6af.jpg",
  "https://graph.org/file/3b1059f85660ed5be4092.jpg",
  "https://graph.org/file/2dec9a542b29deab036ff.jpg",
  "https://graph.org/file/319a8a766f32a9f802e08.jpg",
  "https://graph.org/file/fc0d9364d736ab555f043.jpg",
  "https://graph.org/file/79ec28c9e9deb6181067d.jpg",
    ]
    castle_url = random.choice(castledata)
    await message.reply_photo(castle_url)

add_command_help(
    "•─╼⃝𖠁 Cʜᴇʀʀʏ Bʟᴏssᴏᴍ",
    [
       ["blossom", "Gɪᴠᴇ random Cʜᴇʀʀʏ Bʟᴏssᴏᴍ pic."],
        ],
)
