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

#Legnendx22 Thanks for your Sticker pack 

import random
from pyrogram import Client, filters
from config import SUDO_USERS
from .help import * 

hl = "."

@Client.on_message(
    filters.command(["bc"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def bsdke(client, message):
    args = message.text.split(" ")[1:]
    bsdkedata = [
  "https://graph.org/file/ac866e1d75bdfdb1e2edf.jpg",
  "https://graph.org/file/347eedd9b939c57776f97.jpg",
  "https://graph.org/file/2e51c1cb2ebfaf5b599e0.jpg",
  "https://graph.org/file/a7584d179f380b5627485.jpg",
  "https://graph.org/file/54a3e66e3c30e340cb1fa.jpg",
  "https://graph.org/file/76575287d9fa600d5effb.jpg",
  "https://graph.org/file/a27baae47423663239076.jpg",
  "https://graph.org/file/675a9904801c5bd43bc60.jpg",
    ]
    bsdke_url = random.choice(bsdkedata)
    await message.reply_photo(bsdke_url)

add_command_help(
    "•─╼⃝𖠁 Bᴄ",
    [
       ["bc", "Gɪᴠᴇ random Bᴄ pic."],
        ],
)
