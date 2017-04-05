import discord
import asyncio
from twitch.api import v3 as twitch
from twitch.exceptions import ResourceUnavailableException
from random import randint
import argparse
import requests
import json



client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author != 'BEANBot#8947':
        if message.content.startswith('!info'):
            streamer_html = requests.get('https://api.twitch.tv/kraken/streams/sing_sing?client_id=vpmzqjo3ab8dyeslvz2ia3r3yehif3').json()
            print(streamer_html)
            streamer = json.loads(json.dumps(streamer_html))
            stream_data  = streamer['stream']
            if(stream_data == None):
                reply_message = 'Master Sing is offline. FeelsBadMan'
            else:
                reply_message = 'Master Sing is live - http://www.twitch.tv/sing_sing ' + str(stream_data)
            await client.send_message(message.channel, reply_message)

            
        elif message.content.startswith('!mymmr'):
            mmr = randint(0,9999)
            reply_message = 'Hey ' + str(message.author).split('#', 1)[0]
            reply_message = reply_message + ', your MMR is ' + str(mmr)
            if  mmr > 5999:
                reply_message = reply_message + ' PogChamp'
            else:
                reply_message = reply_message + ' LUL'
            await client.send_message(message.channel, reply_message)

            
        elif message.content.startswith('!mydong'):
            mmr = randint(0,25)
            reply_message = 'Hey ' + str(message.author).split('#', 1)[0]
            reply_message = reply_message + ', your dong hangs '
            reply_message = reply_message + str(mmr)
            reply_message = reply_message + ' cms low Jebaited'
            await client.send_message(message.channel, reply_message)

            
        elif message.content.startswith('!bean'):
            await client.send_message(message.channel, "http://i0.kym-cdn.com/photos/images/facebook/001/166/993/284.png")
        
        
client.run('Mjk2NzI2MjExODE0NjIxMTg2.C72dJw.qgiXa_FvhGX9DY-8pK3ZbzV1FwY')
