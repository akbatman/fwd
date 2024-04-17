import pyrogram
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant, InviteHashExpired, UsernameNotOccupied
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import time
import os
import threading
import json
from os import environ

bot_token = environ.get("TOKEN", "5276059751:AAFCja69AW-EVshgRkqblUXRI95sblvIOTQ") 
api_hash = environ.get("HASH", "bc7a1ff026c4305bcf4f38807aabbec5") 
api_id = environ.get("ID", "11978076")
bot = Client("mybot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

ss = environ.get("STRING", "AQC2xVwAlC8zull3H4CYVr_fnhnxsuv0_dtQqEZTRqGf99-7rBKuPbtakz6rDkfs8PgjmEFqfqLL-k-Ld2-d1KuVCDkb4IwT1HYkExwJbyW7dQrT0ko75ttvNujUOwSMfKowHgeCX4zTqvqXmlCkDImPYcxN_KzmtGP2bi_6PXn_--6sbk3kQEHxcw4i21jFh0-k6j0t-pyZQT7D7Z2VpNchvmGgnCdldMVmi-sFmd9Pyg9hTSqQ8KzhQi_pcz-dM6w4VMKiHLDltpoYpPzXCqp9Sr5UCJ125hl0U15h0dYYdtGJXD1OQ37k9jI5p2rIasBsT5XBJLWigC9uxCy88iGvNjvdMQAAAAE5ywAVAA")
if ss is not None:
    acc = Client("myacc" ,api_id=api_id, api_hash=api_hash, session_string=ss)
    acc.start()
else: acc = None

# download status
def downstatus(statusfile,message):
    while True:
        if os.path.exists(statusfile):
            break

    time.sleep(3)      
    while os.path.exists(statusfile):
        with open(statusfile,"r") as downread:
            txt = downread.read()
        try:
            bot.edit_message_text(message.chat.id, message.id, f"__Downloaded__ : **{txt}**")
            time.sleep(10)
        except:
            time.sleep(5)

# upload status
def upstatus(statusfile,message):
    while True:
        if os.path.exists(statusfile):
            break

    time.sleep(3)      
    while os.path.exists(statusfile):
        with open(statusfile,"r") as upread:
            txt = upread.read()
        try:
            bot.edit_message_text(message.chat.id, message.id, f"__Uploaded__ : **{txt}**")
            time.sleep(10)
        except:
            time.sleep(5)

# progress writter
def progress(current, total, message, type):
    with open(f'{message.id}{type}status.txt',"w") as fileup:
        fileup.write(f"{current * 100 / total:.1f}%")

# start command
@bot.on_message(filters.command(["start"]))
def send_start(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    bot.send_message(message.chat.id, f"**__👋 Hi** **{message.from_user.mention}**, **I am Save Restricted Bot, I can send you restricted content by it's post link__**\n\n{USAGE}",
    reply_markup=InlineKeyboardMarkup([[ InlineKeyboardButton("🌐 Update Channel", url="https://t.me/VJ_Botz")]]), reply_to_message_id=message.id)

# restart command
@bot.on_message(filters.command(["restart"]))
def restart(client, message):
    if message.from_user.id == int(os.getenv("OWNER_ID")):
        bot.send_message(message.chat.id, "Restarting...")
        bot.stop()
    else:
        bot.send_message(message.chat.id, "You are not authorized to use this command.")

@bot.on_message(filters.text)
def save(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    print(message.text)
    ...

USAGE = """**FOR PUBLIC CHATS**
...
"""

bot.run()
