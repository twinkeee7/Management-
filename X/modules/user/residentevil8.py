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
    filters.command(["rs8"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def castle(client, message):
    args = message.text.split(" ")[1:]
    castledata = [
  "https://graph.org/file/78560fa0a4f6443114ac2.jpg",
  "https://graph.org/file/20cf8b023c71ef69385f3.jpg",
  "https://graph.org/file/41cccc37d87b6c7762c90.jpg",
  "https://graph.org/file/20cf8b023c71ef69385f3.jpg",
  "https://graph.org/file/f72e5e311cfedd3304fd0.jpg",
  "https://graph.org/file/e2d1a91ba4f0329313d0f.jpg",
  "https://graph.org/file/d514871860235ddbc49a1.jpg",
  "https://graph.org/file/2936bf39aea5cf17febb0.jpg",
    ]
    castle_url = random.choice(castledata)
    await message.reply_photo(castle_url)

add_command_help(
    "•─╼⃝𖠁 Rᴇsɪᴅᴇɴᴛ8",
    [
       ["rs8", "Gɪᴠᴇ random Rᴇsɪᴅᴇɴᴛ ᴇᴠɪʟ 8 pic."],
        ],
)
