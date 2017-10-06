# @Author: Kazuhiro
# @Date:   2017-10-04T11:35:55+02:00
# @Filename: send.py
# @Last modified by:   Kazuhiro
# @Last modified time: 2017-10-04T11:35:55+02:00


from sys import argv

import discord

from DISC_b.get_channel_id import *

if len(argv) != 2:
    channel_init = 'general'
else:
    channel_init = argv[1]

help_msg = '\n!chan=<channel_name>=<your message>\t| to change channel and send message in there\n'
'!change=<channel_name>\t\t\t| to change only the channel\n'
'!quit\t\t\t\t\t| to quit the program\n'

client = discord.Client()


async def my_background_task():
    await client.wait_until_ready()
    counter = 0
    chan_id = get_channel_id(channel_init, client)
    channel = discord.Object(id=chan_id)
    channel_name = channel_init
    while not client.is_closed:
        counter += 1
        msg = input(channel_name + ' > ')
        if msg == '' or msg == '!help':
            print(help_msg)
            continue
        if msg.startswith('!'):
            if msg == '!quit':
                exit(0)
            elif msg.startswith('!list_chan'):
                list_channels(client)
                continue
            elif msg.startswith('!change='):
                splitted = msg.split('=')
                channel = discord.Object(id=get_channel_id(splitted[1], client))
                channel_name = splitted[1]
                continue
            elif msg.startswith('!chan='):
                splitted = msg.split('=')
                channel = discord.Object(id=get_channel_id(splitted[1], client))
                channel_name = splitted[1]
                msg = splitted[2]
            else:
                continue
        await client.send_message(channel, msg)


@client.event
async def on_ready():
    print('Logged in as ' + client.user.name)
    print('------')


client.loop.create_task(my_background_task())
client.run('') # enter token here
