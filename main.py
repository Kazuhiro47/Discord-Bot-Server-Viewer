# @Author: Kazuhiro
# @Date:   2017-09-28T10:29:47+02:00
# @Filename: test.py
# @Last modified by:   Kazuhiro
# @Last modified time: 2017-09-28T17:22:08+02:00

import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as ' + client.user.name)
    print('------')

@client.event
async def on_message(message):
    if message.channel.name.find('spoil') == -1:
        var = message.timestamp
        datetime_aff = str(var.year) + "/" + str(var.month) + "/" + str(var.day) + " " + str(var.hour) + "h" + str(var.minute) + 'm' + str(var.second) + "s"
        print(datetime_aff + " | " + message.channel.name + " > " + message.author.name + ": " + message.content)

token = '' # insert your token here

client.run(token)
