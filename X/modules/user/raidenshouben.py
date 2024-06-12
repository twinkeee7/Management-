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
    filters.command(["raiden"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def hinata(client, message):
    args = message.text.split(" ")[1:]
    hinatadata = [
  "https://graph.org/file/eb0446474b90145fe1dc0.jpg",
  "https://graph.org/file/b7a31e8712cd6ca1e6c69.jpg",
  "https://graph.org/file/ac29896bf3f601ad47c6e.jpg",
  "https://graph.org/file/c0770646fd3b3f8ac92af.jpg",
  "https://graph.org/file/a54bd529c2a53c9b8b063.jpg",
  "https://graph.org/file/3175fc67a421991e18200.jpg",
  "https://graph.org/file/eb0446474b90145fe1dc0.jpg",
  "https://graph.org/file/ac29896bf3f601ad47c6e.jpg",
    ]
    hinata_url = random.choice(hinatadata)
    await message.reply_photo(hinata_url)

add_command_help(
    "•─╼⃝𖠁 Rᴀɪᴅᴇɴ",
    [
       ["raiden", "Gɪᴠᴇ random Rᴀɪᴅᴇɴ Sʜᴏᴜʙᴇɴ pic."],
        ],
)
