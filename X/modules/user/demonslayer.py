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
    filters.command(["demon"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def demon(client, message):
    args = message.text.split(" ")[1:]
    demondata = [
  "https://graph.org/file/bfb2ebcd0f28e14de5c21.jpg",
  "https://graph.org/file/68e0ce5c311dd2318c6a0.jpg",
  "https://graph.org/file/c8f38d5bf6440ef6a3c5f.jpg",
  "https://graph.org/file/d7aaef7627682856feb63.jpg",
  "https://graph.org/file/6fab72d5f69ba4fdfd341.jpg",
  "https://graph.org/file/89ff44f7d9045fbaeffc1.jpg",
  "https://graph.org/file/89ff44f7d9045fbaeffc1.jpg",
  "https://graph.org/file/691790c56ca074047b6fb.jpg",
    ]
    demon_url = random.choice(demondata)
    await message.reply_photo(demon_url)

add_command_help(
    "•─╼⃝𖠁 Dᴇᴍᴏɴ Sʟᴀʏᴇʀ",
    [
       ["demon", "Gɪᴠᴇ random Dᴇᴍᴏɴ Sʟᴀʏᴇʀ pic."],
        ],
)
