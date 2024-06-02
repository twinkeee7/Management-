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


import asyncio
from random import choice
from pyrogram.types import Message
from pyrogram import filters, Client
from config import OWNER_ID
from config import SUDO_USERS
from config import CMD_HANDLER as cmd
from XDB.data import GROUP, SPORMS
from .help import *

@Client.on_message(
    filters.command(["porm"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def porm(client: Client, message: Message):
    cid = message.chat.id
    if int(cid) in GROUP:
        await message.reply_text("𝐬𝐫𝐲, 𝐭𝐡𝐢𝐬 𝐠𝐫𝐩 𝐢𝐬 𝐩𝐫𝐨𝐭𝐞𝐜𝐭𝐞𝐝 𝐛𝐲 𝐬𝐨𝐦𝐞 𝐯𝐢𝐬𝐮𝐚𝐥 𝐩𝐨𝐰𝐞𝐫𝐬 🛡️")
        return

    altp = message.text.split(" ", 2)
    if len(altp) > 1:
        quantity = int(altp[1])
        for _ in range(quantity):
            porm = choice(SPORMS)
            await client.send_video(cid, porm)
            await asyncio.sleep(0.3)
    else:
        await message.reply_text(f".𝐩𝐨𝐫𝐦 13")


add_command_help(
    "•─╼⃝𖠁 Aᴅᴜʟᴛ Zᴏɴᴇ",
    [
        ["porm", "Tᴏ ꜱᴇɴᴅ ᴘᴏʀɴ ᴠɪᴅᴇᴏ."],
    ],
)
