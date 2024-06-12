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
    filters.command(["rs4"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def castle(client, message):
    args = message.text.split(" ")[1:]
    castledata = [
  "https://graph.org/file/d326009f34a278f2eaefa.jpg",
  "https://graph.org/file/292694369e9c2d6ad56ad.jpg",
  "https://graph.org/file/f1b8cf4a6ab67c63f1700.jpg",
  "https://graph.org/file/28816e1bab602fe780bdf.jpg",
  "https://graph.org/file/7560c6d0590223fe34c2d.jpg",
  "https://graph.org/file/9f194858f64904bb675df.jpg",
  "https://graph.org/file/d326009f34a278f2eaefa.jpg",
  "https://graph.org/file/292694369e9c2d6ad56ad.jpg",
    ]
    castle_url = random.choice(castledata)
    await message.reply_photo(castle_url)

add_command_help(
    "•─╼⃝𖠁 Rᴇsɪᴅᴇɴᴛ4",
    [
       ["rs4", "Gɪᴠᴇ random Rᴇsɪᴅᴇɴᴛ ᴇᴠɪʟ 4 ʀᴇᴍᴀᴋᴇ pic."],
        ],
)
