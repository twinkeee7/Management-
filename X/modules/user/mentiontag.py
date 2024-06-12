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

# Copyright (C) 2020-2021 by Toni880@Github, < https://github.com/Toni880 >.
#
# This file is part of < https://github.com/Toni880/Prime-Userbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Toni880/Prime-Userbot/blob/master/LICENSE >
#
# All rights reserved. Ken-Kan

# REMAKE BY NOBITA XD AND TRYTOLIVEALONE 


from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message
from X.helpers.tools import get_arg
from config import SUDO_USERS
from X import *
from config import CMD_HANDLER

from .help import *

spam_chats = []


@Client.on_message(
    filters.command(["mentionall"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def mentionall(client: Client, message: Message):
    await message.delete()
    chat_id = message.chat.id
    direp = message.reply_to_message
    args = get_arg(message)
    if not direp and not args:
        return await message.edit("**Drop me a message or reply to a message!**")

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}), "
        if usrnum == 5:
            if args:
                txt = f"{args}\n\n{usrtxt}"
                await client.send_message(chat_id, txt)
            elif direp:
                await direp.reply(usrtxt)
            await sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@Client.on_message(
    filters.command(["cancel"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def cancel_spam(client: Client, message: Message):
    if not message.chat.id in spam_chats:
        return await message.edit("**Looks like there's no tagall here.**")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.edit("**Stop Mention.**") 


add_command_help(
    "•─╼⃝𖠁 Mᴇɴᴛɪᴏɴᴀʟʟ",
    [
       ["mentionall", "Mᴇɴᴛɪᴏɴ ᴀʟʟ Mᴇᴍʙᴇʀs ɪɴ ᴛʜᴇ ᴄʜᴀᴛ."],
       ["cancel", "Tᴏ Cᴀɴᴄᴇʟ Mᴇɴᴛɪᴏɴ ᴀʟʟ Mᴇssᴀɢᴇ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ."],
        ],
)
