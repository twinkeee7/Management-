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
    filters.command(["night"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def morning(client, message):
    args = message.text.split(" ")[1:]
    morningdata = [
  "https://graph.org/file/f9ad8aaf219cd012bf4f8.jpg",
  "https://graph.org/file/ce4d836a558e652cf81a5.jpg",
  "https://graph.org/file/32cb1f583552f55649809.jpg",
  "https://graph.org/file/63e15763f933af7bbaaf9.jpg",
  "https://graph.org/file/b2c21f6febb4048b2c32e.jpg",
  "https://graph.org/file/f9ad8aaf219cd012bf4f8.jpg",
  "https://graph.org/file/32cb1f583552f55649809.jpg",
  "https://graph.org/file/ce4d836a558e652cf81a5.jpg",
    ]
    morning_url = random.choice(morningdata)
    await message.reply_photo(morning_url)

add_command_help(
    "•─╼⃝𖠁 Gᴏᴏᴅ Nɪɢʜᴛ",
    [
       ["night", "Gɪᴠᴇ random Gᴏᴏᴅ Nɪɢʜᴛ pic."],
        ],
)
