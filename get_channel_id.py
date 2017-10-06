# @Author: Kazuhiro
# @Date:   2017-10-04T12:02:40+02:00
# @Filename: get_channel_id.py
# @Last modified by:   Kazuhiro
# @Last modified time: 2017-10-04T12:02:40+02:00

import sys


def get_channel_id(name, client):

    for chann in client.get_all_channels():
        chan_id = chann.id
        if chann.name == name:
            return chan_id
    print('\nChannel not found')


def list_channels(client):

    for channel in client.get_all_channels():
        try:
            print(channel.name)
        except UnicodeEncodeError:
            print(channel.name.encode(sys.stdout.encoding, errors='replace'))
