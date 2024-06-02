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
    filters.command(["japanese"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def japanese(client, message):
    args = message.text.split(" ")[1:]
    japanesedata = [
  "https://graph.org/file/edf6ce5502aff51b49c29.jpg",
  "https://graph.org/file/1cd81b8c13b2cea7e3a92.jpg",
  "https://graph.org/file/4045e6d08388d79c235b5.jpg",
  "https://graph.org/file/1b317d2306735cd835635.jpg",
  "https://graph.org/file/a5c7c835e6f8d688469a0.jpg",
  "https://graph.org/file/06db07b74e2c8481f2150.jpg",
  "https://graph.org/file/0e1d08c568f057b0da5d0.jpg",
  "https://graph.org/file/edf6ce5502aff51b49c29.jpg",
    ]
    japanese_url = random.choice(japanesedata)
    await message.reply_photo(japanese_url)

add_command_help(
    "•─╼⃝𖠁 Jᴀᴘᴀɴᴇsᴇ",
    [
       ["japanese", "Gɪᴠᴇ random Jᴀᴘᴀɴᴇsᴇ X Usᴇʀʙᴏᴛ pic."],
        ],
)
