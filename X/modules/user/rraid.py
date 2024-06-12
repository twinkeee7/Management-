# MIT License
# Copyright (c) 2024 Japanese-X-Userbot
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID, SUDO_USERS, CMD_HANDLER as cmd
from XDB.data import RAID, MASTERS

reply_raid_users = []

@Client.on_message(filters.command(["rraid", "replyraid"], cmd) & (filters.me | filters.user(SUDO_USERS)))
async def activate_reply_raid(client: Client, message: Message):
    global reply_raid_users
    args = message.text.split()

    if len(args) > 1:
        user = await client.get_users(args[1])
        user_id = user.id
    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    else:
        await message.reply_text(f"{cmd}rraid <username> or reply to a user")
        return

    if user_id in MASTERS:
        await message.reply_text("Nope, this guy is an owner ☠️")
    elif user_id == OWNER_ID:
        await message.reply_text("Nope, this guy is the owner of these bots 🥀")
    elif user_id in SUDO_USERS:
        await message.reply_text("Nope, this guy is a sudo user 💗")
    else:
        reply_raid_users.append(user_id)
        await message.reply_text("Activated reply raid ✅")

@Client.on_message(filters.command(["drraid", "draid", "dreplyraid"], cmd) & (filters.me | filters.user(SUDO_USERS)))
async def deactivate_reply_raid(client: Client, message: Message):
    global reply_raid_users
    args = message.text.split()

    if len(args) > 1:
        user = await client.get_users(args[1])
        user_id = user.id
    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    else:
        await message.reply_text(f"{cmd}drraid <username> or reply to a user")
        return

    if user_id in reply_raid_users:
        reply_raid_users.remove(user_id)
        await message.reply_text("Reply raid de-activated ✅")

@Client.on_message(~filters.me & filters.incoming)
async def reply_raid_watcher(client: Client, message: Message):
    global reply_raid_users
    user_id = message.from_user.id

    if user_id in reply_raid_users:
        reply_text = choice(RAID)
        await message.reply_text(reply_text)
