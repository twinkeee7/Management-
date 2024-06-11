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

 

import requests
from pyrogram import filters, Client
from config import SUDO_USERS

from .help import * 


def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    if to_currency in data['rates']:
        rate = data['rates'][to_currency]
        converted_amount = amount * rate
        return converted_amount
    else:
        return None

# Command to convert currency
@Client.on_message(
    filters.command(["currency"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def convert_command(client, message):
    try:
        # Parse command
        command = message.text.split()
        amount = float(command[1])
        from_currency = command[2].upper()
        to_currency = command[3].upper()

        # Convert currency
        converted_amount = convert_currency(amount, from_currency, to_currency)

        # Send result
        if converted_amount:
            await message.reply(f"{amount} {from_currency} is approximately {converted_amount:.2f} {to_currency}")
        else:
            await message.reply("Sorry, unable to convert. Please check your input currencies.")
    except Exception as e:
        await message.reply("Invalid command. Please use /convert <amount> <from_currency> <to_currency>")

