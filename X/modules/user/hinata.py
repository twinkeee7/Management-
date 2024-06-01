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
    filters.command(["hinata"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def hinata(client, message):
    args = message.text.split(" ")[1:]
    hinatadata = [
  "https://graph.org/file/6851f728d2378426c543b.jpg",
  "https://graph.org/file/86059f15b7345f135d303.jpg",
  "https://graph.org/file/94d6c15b9fc6d92e8b5c8.jpg",
  "https://graph.org/file/12d3f519481a086dfabb4.jpg",
  "https://graph.org/file/a636ffa711ed3fe1148fe.jpg",
  "https://graph.org/file/7b9d3b1028712377569b6.jpg",
  "https://graph.org/file/17c301cfd5dc72c2ec4a1.jpg",
  "https://graph.org/file/f3a3d3065606acf2a7c12.jpg",
    ]
    hinata_url = random.choice(hinatadata)
    await message.reply_photo(hinata_url)

add_command_help(
    "•─╼⃝𖠁 Hɪɴᴀᴛᴀ",
    [
       ["hinata", "Gɪᴠᴇ random Hɪɴᴀᴛᴀ pic."],
        ],
)
