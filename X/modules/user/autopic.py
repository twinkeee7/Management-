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

# Credit : Zaid Userbot 

#REMAKE BY : NOBITA XD
#DON'T KANG FUCKING COWARD
#BSDKE KANG KIYA TOH SOCH LIYO
#AAG LAGA DUNGA TERE ANDAR 
#SAMJHA ? 

import asyncio
from datetime import datetime
from pathlib import Path
from random import choice
from shutil import copyfile

from PIL import Image, ImageDraw, ImageFont
from pyrogram import filters, Client
from config import OWNER_ID
from config import SUDO_USERS
from X.helpers.basic import eor
from .help import *


__XOR = []
FIRST_TIME = True
DIM = [(100, 200), (1280, 200), (1280, 1600), (100, 1600)]


async def _autopic(_, delay):
    global FIRST_TIME

    while bool(__XOR):
        await asyncio.sleep(delay)
        original = "X/resources/autopic-template.jpg"
        photo = "pic.png"
        copyfile(original, photo)
        current_time = datetime.now().strftime(
            f'%H:%M %d-%m-%y\nLife Is too short\nto argue.\njust say "fuck off"\nand move on.'
        )
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype("X/resources/autopic-font-ubuntu.ttf", 60)
        drawn_text.text(choice(DIM), current_time, font=fnt, fill=(0, 0, 0))
        img.save(photo)
        try:
            if not FIRST_TIME:
                async for pic in _.get_chat_photos("me", limit=1):
                    await _.delete_profile_photos(pic.file_id)
                    await asyncio.sleep(2)
            await _.set_profile_photo(photo=photo)
            FIRST_TIME = False
        except Exception as exc:
            print("Autopic Error: " + exc)
        finally:
            Path(photo).unlink()


@Client.on_message(
    filters.command(["autopic"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def autopic_zaid(_, m):
    global __XOR
    arc = await eor(m, "...")
    if bool(__XOR):
        __XOR[0].cancel()
        t = "`Autopic Stopped Successfully.`"
        __XOR.clear()
    else:
        _task = _autopic(_, delay=300)
        task = asyncio.create_task(_task)
        __XOR.append(task)
        t = "`Started Autopic.`"
    await arc.edit_text(t)


add_command_help(
    "•─╼⃝𖠁 Aᴜᴛᴏ ᴘɪᴄ",
    [
       ["autopic", "Cʜᴀɴɢᴇ ʏᴏᴜʀ DP ᴇᴠᴇʀʏ 5 ᴍɪɴᴜᴛᴇ Iғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴛᴏᴘ ᴀᴜᴛᴏ ᴘɪᴄ ᴛʀʏ ᴀᴜᴛᴏᴘɪᴄ ᴀɢᴀɪɴ ᴛᴏ sᴛᴏᴘ ɪᴛ."],
        ],
)
