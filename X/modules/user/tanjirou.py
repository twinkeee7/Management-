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
    filters.command(["tanjirou"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def demon(client, message):
    args = message.text.split(" ")[1:]
    demondata = [
  "https://graph.org/file/a484e26bbd9b6f8757426.jpg",
  "https://graph.org/file/caea011b326ecf637fcda.jpg",
  "https://graph.org/file/2673b2b68f63ad7483f5b.jpg",
  "https://graph.org/file/ec50f6a102ad36411f70e.jpg",
  "https://graph.org/file/fddc28fc2e8d856f572c4.jpg",
  "https://graph.org/file/fddc28fc2e8d856f572c4.jpg",
  "https://graph.org/file/8b635492173f1541c7d3b.jpg",
  "https://graph.org/file/2673b2b68f63ad7483f5b.jpg",
    ]
    demon_url = random.choice(demondata)
    await message.reply_photo(demon_url)

add_command_help(
    "•─╼⃝𖠁 Tᴀɴᴊɪʀᴏᴜ",
    [
       ["tanjirou", "Gɪᴠᴇ random Kᴀᴍᴀᴅᴏ Tᴀɴᴊɪʀᴏᴜ Sʟᴀʏᴇʀ pic."],
        ],
)
