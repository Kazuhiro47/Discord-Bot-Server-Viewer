# @Author: Kazuhiro
# @Date:   2017-09-28T10:29:47+02:00
# @Filename: test.py
# @Last modified by:   Kazuhiro
# @Last modified time: 2017-10-03T14:23:46+02:00

import sys

import discord

client = discord.Client()

names = dict()


@client.event
async def on_ready():
    connected_member = 0
    for serv in client.servers:
        for lab_mem in serv.members:
            names[lab_mem.id] = lab_mem.name
            if lab_mem.status.name != 'offline':
                name = lab_mem.name
                try:
                    print(name)
                except UnicodeEncodeError:
                    print(name.encode(sys.stdout.encoding,
                                      errors='replace'))
                connected_member += 1

    print('Logged in as ' + client.user.name)
    print('Currently ' + str(connected_member) +
          ' members on server\n------')


@client.event
async def on_message(message):
    chans_exceptions = ['']
    if message.channel.name in chans_exceptions or message.channel.name.find(
            'spoil') == -1:
        var = message.timestamp
        datetime_aff = str(var.year) + "/" + str(var.month) + "/" + str(
            var.day) + " " + str(var.hour) + "h" + str(
            var.minute) + 'm' + str(var.second) + "s"
        try:
            msg = datetime_aff + " | " + message.channel.name + " > " + \
                  message.author.name + ": " + message.content
            for name_id in names.keys():
                msg = msg.replace(name_id, names[name_id])
            print(msg)
        except UnicodeEncodeError:
            msg = datetime_aff + " | " + message.channel.name + " > " + \
                  message.author.name + ": " + message.content
            msg = msg.encode(sys.stdout.encoding, errors='replace')
            print(msg)


# insert your token here
token = ''

client.run(token)
