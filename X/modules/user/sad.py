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
    filters.command(["sad"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def castle(client, message):
    args = message.text.split(" ")[1:]
    castledata = [
  "https://graph.org/file/1fbf1067783766f94ffd9.jpg",
  "https://graph.org/file/936d84cb14c8b2fdb7ae6.jpg",
  "https://graph.org/file/32cd9e2af39313214eb07.jpg",
  "https://graph.org/file/05e88df4373abd287b528.jpg",
  "https://graph.org/file/eadd8ce5faabceda933f9.jpg",
  "https://graph.org/file/8f20b6546a0487eecbaed.jpg",
  "https://graph.org/file/9cee901c0fd8c3793eb0e.jpg",
  "https://graph.org/file/44f5282dfd2345a597a1b.jpg",
  "https://graph.org/file/ac1046936f1a681b6c610.jpg",
  "https://graph.org/file/ac1046936f1a681b6c610.jpg",
  "https://graph.org/file/13f5c42aaf324143af205.jpg",
  "https://graph.org/file/7484e4d6b8e8c300be3a7.jpg",
  "https://graph.org/file/166fc6b9878a803763947.jpg",
  "https://graph.org/file/ba4c13bd22b48327c57b1.jpg",
  "https://graph.org/file/edafa7266f9ad3e3fe4e3.jpg",
  "https://graph.org/file/c478e54b027809de8fa5c.jpg",
    ]
    castle_url = random.choice(castledata)
    await message.reply_photo(castle_url)

add_command_help(
    "•─╼⃝𖠁 Sᴀᴅ",
    [
       ["sad", "Gɪᴠᴇ random Sᴀᴅ pic."],
        ],
)
