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
    filters.command(["nezuko"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def nezuko(client, message):
    args = message.text.split(" ")[1:]
    nezukodata = [
  "https://graph.org/file/55103e5cb0177f358cf58.jpg",
  "https://graph.org/file/413a0286008fe951e68ba.jpg",
  "https://graph.org/file/9e590e50dc1608d27d581.jpg",
  "https://graph.org/file/2c622c6e77057c85463e7.jpg",
  "https://graph.org/file/1a14904bc7465b25965d5.jpg",
  "https://graph.org/file/8f63eada971a6eb82307c.jpg",
  "https://graph.org/file/54a295caff124bc28bbff.jpg",
  "https://graph.org/file/55103e5cb0177f358cf58.jpg",
    ]
    nezuko_url = random.choice(nezukodata)
    await message.reply_photo(nezuko_url)

add_command_help(
    "•─╼⃝𖠁 Nᴇᴢᴜᴋᴏ",
    [
       ["nezuko", "Gɪᴠᴇ random Nᴇᴢᴜᴋᴏ pic."],
        ],
  )
