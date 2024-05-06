import heroku3
from os import getenv
from config import SUDO_USERS 
from config import OWNER_ID
from config import HEROKU_APP_NAME, HEROKU_API_KEY
from pyrogram import Client, filters
from pyrogram.types import Message

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
