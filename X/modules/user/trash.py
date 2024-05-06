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
#SOFTWARE

import heroku3
from os import getenv
from config import SUDO_USERS 
from config import OWNER_ID
from config import HEROKU_APP_NAME
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from config import HEROKU_API_KEY

@Client.on_message(
    filters.command(["sudolist"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def gbanlist(client: Client, message: Message):
    users = SUDO_USERS
    ex = await message.edit_text("ᴘʀᴏᴄᴇꜱꜱɪɴɢ...")
    if not users:
        return await ex.edit("ɴᴏ ᴜꜱᴇʀꜱ ʜᴀᴠᴇ ʙᴇᴇɴ ꜱᴇᴛ ʏᴇᴛ")
    gban_list = "**sᴜᴅᴏ ᴜꜱᴇʀs:**\n"
    count = 0
    for i in users:
        count += 1
        gban_list += f"**{count}** `{i}`\n"
    return await ex.edit(gban_list)

@Client.on_message(
    filters.command(["addsudo"], ".") & (filters.me | filters.user(OWNER_ID))
)
async def add_sudo(_, message: Message):
       if not message.reply_to_message:
              await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ")
              return
       elif HEROKU_APP_NAME is None:
              await message.reply_text("[ʜᴇʀᴏᴋᴜ]:" "\nᴘʟᴇᴀꜱᴇ ꜱᴇᴛᴜᴘ ʏᴏᴜʀ **ʜᴇʀᴏᴋᴜ_ᴀᴘᴘ_ɴᴀᴍᴇ**")
              return
       elif HEROKU_API_KEY is None:
              await message.reply_text("[ʜᴇʀᴏᴋᴜ]:" "\nᴘʟᴇᴀꜱᴇ ꜱᴇᴛᴜᴘ ʏᴏᴜʀ **ʜᴇʀᴏᴋᴜ_ᴀᴘɪ_ᴋᴇʏ**")
              return
       else:
              heroku = heroku3.from_key(HEROKU_API_KEY)
              app = heroku.app(HEROKU_APP_NAME)

       ok = await message.reply_text(f"ᴀᴅᴅɪɴɢ ᴜꜱᴇʀ ᴀꜱ ꜱᴜᴅᴏ")
       heroku_var = app.config()

       sudousers = getenv("SUDO_USERS")
       target = message.reply_to_message.from_user.id
       if len(sudousers) > 0:
              newsudo = f"{sudousers} {target}"
       else:
              newsudo = f"{target}"
       await ok.edit(f"**ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ**: `{target}`\nʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...")
       heroku_var["SUDO_USERS"] = newsudo 
