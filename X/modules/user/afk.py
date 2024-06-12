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

# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de


#REMAKE BY : NOBITA XD 

import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from X import BOTLOG_CHATID
from X.helpers.msg_types import Types, get_message_type
from X.helpers.parser import escape_markdown, mention_markdown
from X.helpers.SQL.afk_db import get_afk, set_afk
from .help import *

# Set priority to 11 and 12
MENTIONED = []
AFK_RESTIRECT = {}
DELAY_TIME = 3  # seconds


@Client.on_message(filters.me & filters.command("afk", cmd))
async def afk(client: Client, message: Message):
    if len(message.text.split()) >= 2:
        set_afk(True, message.text.split(None, 1)[1])
        await message.edit(
            "❏ {} <b>Aʟʀᴇᴀᴅʏ AFK!</b>\n└ <b>Bᴇᴄᴀᴜꜱᴇ:</b> <code>{}</code>".format(
                mention_markdown(message.from_user.id, message.from_user.first_name),
                message.text.split(None, 1)[1],
            )
        )
    else:
        set_afk(True, "")
        await message.edit(
            "✘ {} <b>Aʟʀᴇᴀᴅʏ AFK</b> ✘".format(
                mention_markdown(message.from_user.id, message.from_user.first_name)
            )
        )
    await message.stop_propagation()


@Client.on_message(
    (filters.mentioned | filters.private) & filters.incoming & ~filters.bot, group=11
)
async def afk_mentioned(client: Client, message: Message):
    global MENTIONED
    get = get_afk()
    if get and get["afk"]:
        if "-" in str(message.chat.id):
            cid = str(message.chat.id)[4:]
        else:
            cid = str(message.chat.id)

        if cid in list(AFK_RESTIRECT):
            if int(AFK_RESTIRECT[cid]) >= int(time.time()):
                return
        AFK_RESTIRECT[cid] = int(time.time()) + DELAY_TIME
        if get["reason"]:
            await message.reply(
                "❏ {} <b>Cᴜʀʀᴇɴᴛʟʏ AFK!</b>\n└ <b>Bᴇᴄᴀᴜꜱᴇ:</b> <code>{}</code>".format(
                    client.me.mention, get["reason"]
                )
            )
        else:
            await message.reply(
                f"<b>Sᴏʀʀʏ</b> {client.me.first_name} <b>Currently AFK!</b>"
            )

        _, message_type = get_message_type(message)
        if message_type == Types.TEXT:
            if message.text:
                text = message.text
            else:
                text = message.caption
        else:
            text = message_type.name

        MENTIONED.append(
            {
                "user": message.from_user.first_name,
                "user_id": message.from_user.id,
                "chat": message.chat.title,
                "chat_id": cid,
                "text": text,
                "message_id": message.id,
            }
        )
        try:
            await client.send_message(
                BOTLOG_CHATID,
                "<b>#MENTION\n • Fʀᴏᴍ :</b> {}\n • <b>Gʀᴏᴜᴘ :</b> <code>{}</code>\n • <b>Mᴇꜱꜱᴀɢᴇ :</b> <code>{}</code>".format(
                    message.from_user.mention,
                    message.chat.title,
                    text[:3500],
                ),
            )
        except BaseException:
            pass


@Client.on_message(filters.me & filters.group, group=12)
async def no_longer_afk(client: Client, message: Message):
    global MENTIONED
    get = get_afk()
    if get and get["afk"]:
        set_afk(False, "")
        try:
            await client.send_message(BOTLOG_CHATID, "Yᴏᴜ ᴀʀᴇ ɴᴏ ʟᴏɴɢᴇʀ AFK!")
        except BaseException:
            pass
        text = "<b>Tᴏᴛᴀʟ {} Mᴇɴᴛɪᴏɴ Mᴏᴍᴇɴᴛ Cᴜʀʀᴇɴᴛʟʏ AFK<b>\n".format(len(MENTIONED))
        for x in MENTIONED:
            msg_text = x["text"]
            if len(msg_text) >= 11:
                msg_text = "{}...".format(x["text"])
            text += "- [{}](https://t.me/c/{}/{}) ({}): {}\n".format(
                escape_markdown(x["user"]),
                x["chat_id"],
                x["message_id"],
                x["chat"],
                msg_text,
            )
        try:
            await client.send_message(BOTLOG_CHATID, text)
        except BaseException:
            pass
        MENTIONED = []


add_command_help(
    "•─╼⃝𖠁 Aғᴋ",
    [
       ["afk", "Sᴇɴᴅ ᴀᴡᴀʏ ғʀᴏᴍ ᴋᴇʏʙᴏᴀʀᴅ ᴍᴇssᴀɢᴇ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ."],
        ],
)
