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

from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as kaz
from pyrogram.errors import MessageNotModified
from X.helpers.basic import *
from X.helpers.adminHelpers import DEVS
from config import *
from config import CMD_HANDLER
from config import SUDO_USERS
from X.utils import *
from urllib.parse import quote

import requests
import os
import json
import random

from .help import *

# Updated API details
API_ENDPOINT = "https://spotify-downloader8.p.rapidapi.com/api/spotify"
API_KEY = "5eb5f408"
RAPIDAPI_KEY = "d19c1c0167mshbfca18a47fb33a0p14552ejsn9b47b7ac383a"
RAPIDAPI_HOST = "spotify-downloader8.p.rapidapi.com"

@Client.on_message(
    filters.command(["spotify"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def spotify_downloader(client: Client, message: Message):
    if len(message.command) == 1:
        return await message.reply(f"Ketik <code>.{message.command[0]} [Spotify URL]</code> to download a Spotify track")
    
    Spotifyurl = message.text.split(" ", maxsplit=1)[1]
    
    msg = await message.reply("`Downloading...`")

    stages = ["Downloading.", "Downloading..", "Downloading...", "Downloading..", "Downloading."]
    
    for stage in stages:
        await asyncio.sleep(0.5)
        await msg.edit(stage)
    
    querystring = {"apikey": API_KEY, "search": Spotifyurl}
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST
    }
    
    try:
        response = requests.get(API_ENDPOINT, headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()
        
        if "download_url" in data:
            download_url = data["download_url"]
            await msg.edit(f"Download link: [hidden]({download_url})")
            await message.reply(
                f"Title: {data.get('title', 'Unknown Title')}\n"
                f"Artist: {data.get('artist', 'Unknown Artist')}\n"
                f"Duration: {data.get('time', '00:00')}"
            )
        else:
            await msg.edit("Failed to retrieve the download URL. Please try again later.")
    except Exception as e:
        await msg.edit(f"Error: {str(e)}")
    
    await message.delete()
    
    


add_command_help(
    "•─╼⃝𖠁 Sᴘᴏᴛɪғʏ",
    [
       ["spotify", "Sᴇɴᴅ Sᴘᴏᴛɪғʏ Sᴏɴɢ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ."],
        ],
)
