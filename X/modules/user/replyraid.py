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


#Credit Japanese X Userbot & Storm Userbot 

#NOBITA XD AND KEXX (KUNAL)


import asyncio
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from XDB.data import MASTERS, RAID
from config import SUDO_USERS, OWNER_ID

from .help import * 


@Client.on_message(
    filters.command(["rraid", "replyraid"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def rraid(x: Client, message: Message):
    global rusers
    kex = message.text.split(" ")

    if len(kex) > 1:
        ok = await x.get_users(kex[1])
        id = ok.id
        if id in MASTERS:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ Jᴀᴘᴀɴᴇsᴇ ᴏᴡɴᴇʀ ☠️")
        elif id == OWNER_ID:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ 🥀")
        elif id in SUDO_USERS:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏꜱ ɪꜱ ꜱᴜᴅᴏ ᴜꜱᴇʀ 💗")
        else:
            rusers.append(id)
            await message.reply_text("ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ ✅")

    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        if user_id in MASTERS:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ Jᴀᴘᴀɴᴇsᴇ ᴏᴡɴᴇʀ ☠️")
        elif user_id == OWNER_ID:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ 🥀")
        elif user_id in SUDO_USERS:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏꜱ ɪꜱ ꜱᴜᴅᴏ ᴜꜱᴇʀ 💗")
        else:
            rusers.append(user_id)
            await message.reply_text("» ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ ✅")

    else:
        await message.reply_text(".ʀʀᴀɪᴅ <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")

@Client.on_message(
    filters.command(["drraid", "draid", "dreplyraid"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def draid(x: Client, message: Message):
    global rusers
    kex = message.text.split(" ")

    if len(kex) > 1:
        ok = await x.get_users(kex[1])
        id = ok.id
        if id in rusers:
            rusers.remove(id)
            await message.reply_text("ʀᴇᴘʟʏ ʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ ✅")

    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        ok = await x.get_users(user_id)
        id = ok.id
        if id in rusers:
            rusers.remove(id)
            await message.reply_text("ʀᴇᴘʟʏ ʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ ✅")

    else:
        await message.reply_text(".ᴅʀʀᴀɪᴅ <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")

@Client.on_message(~filters.me & filters.incoming)
async def watcher(_, msg: Message):
    global rusers
    id = msg.from_user.id
    if id in rusers:
        reply = choice(RAID)
        await msg.reply_text(reply)


add_command_help(
    "•─╼⃝𖠁 Rᴇᴘʟʏ ʀᴀɪᴅ",
    [
        ["rraid", "Tᴏ ꜱᴇɴᴅ Rᴇᴘʟʏ ʀᴀɪᴅ."],
        ["drraid", "To Deactivate Rᴇᴘʟʏ ʀᴀɪᴅ"],
    ],
)
