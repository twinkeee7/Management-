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
    filters.command(["hiroshima"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def hinata(client, message):
    args = message.text.split(" ")[1:]
    hinatadata = [
  "https://graph.org/file/f6d545de22d75795850df.jpg",
  "https://graph.org/file/f3a25c75cdf4e157ae73c.jpg",
  "https://graph.org/file/a227f1de448ea4842b8f3.jpg",
  "https://graph.org/file/bdbdb35b7202fcba1003d.jpg",
  "https://graph.org/file/ebc4f511d30ab10b9aa05.jpg",
  "https://graph.org/file/a64c485fdc99588e421b8.jpg",
  "https://graph.org/file/a227f1de448ea4842b8f3.jpg",
  "https://graph.org/file/f3a25c75cdf4e157ae73c.jpg",
    ]
    hinata_url = random.choice(hinatadata)
    await message.reply_photo(hinata_url)

add_command_help(
    "•─╼⃝𖠁 Hɪʀᴏsʜɪᴍᴀ",
    [
       ["hiroshima", "Gɪᴠᴇ random Hɪʀᴏsʜɪᴍᴀ pic."],
        ],
)
