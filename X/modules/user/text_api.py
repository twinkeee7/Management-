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


from aiohttp.client_exceptions import ClientError
from pyrogram import filters, Client 
from pyrogram.types import Message

from config import SUDO_USERS
from X.helpers.aiohttp_helper import AioHttp
from .help import *

text_apis_data = {
    "compliment": {
        "url": "https://complimentr.com/api",
        "target_key": "compliment",
        "help": "Sends a nice compliment.",
    },
    "devexcuse": {
        "url": "https://api.devexcus.es/",
        "target_key": "text",
        "help": "It works on my machine!",
    },
    "insult": {
        "url": "https://evilinsult.com/generate_insult.php?lang=en",
        "target_key": "insult",
        "help": "Give it a guess dumbass!",
    },
    "kanye": {
        "url": "https://api.kanye.rest/",
        "target_key": "quote",
        "format": "Kanye once said:\n`{}`",
        "help": "Kanye used to say",
    },
    "programmer": {
        "url": "http://quotes.stormconsultancy.co.uk/random.json",
        "target_key": "quote",
        "help": "Programmers be like.",
    },
    "affirmation": {
        "url": "https://www.affirmations.dev/",
        "target_key": "affirmation",
        "help": "Affirmative messages",
    },
}

text_api_commands = []
for x in text_apis_data:
    text_api_commands.append(x)
    if "alts" in text_apis_data[x]:
        for y in text_apis_data[x]["alts"]:
            text_api_commands.append(y)


@Client.on_message(
    filters.command(text_api_commands, ".") & (filters.me | filters.user(SUDO_USERS))
)
async def text_api(bot: Client, message: Message):
    cmd = message.command
    api_key = cmd[0]
    api = text_apis_data[api_key]

    try:
        try:
            data = await AioHttp().get_json(api["url"])
            resp_json = data[api["target_key"]]
            if "format" in api:
                txt = api["format"].format(resp_json)
            else:
                txt = resp_json.capitalize()
            if message.from_user.is_self:
                await message.edit(txt)
            else:
                await message.reply(txt)
        except Exception:
            data = await AioHttp().get_text(api["url"])
            if message.from_user.is_self:
                await message.edit(data)
            else:
                await message.reply(data)
    except ClientError as e:
        print(e)
        await message.delete()


# Command help section
for x in text_apis_data:
    add_command_help(
        "•─╼⃝𖠁 Tᴇxᴛ",
        [
            [f".{x}", text_apis_data[x]["help"]],
        ],
              )
