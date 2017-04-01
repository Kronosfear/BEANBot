import discord
import asyncio
from twitch.api import v3 as twitch
from twitch.exceptions import ResourceUnavailableException
from random import randint
import argparse
import requests
import json



client = discord.Client()


async def my_background_task():
    await client.wait_until_ready()
    channel = discord.Object(id='292869746293211146')
    while not client.is_closed:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        streamer_html = requests.get('https://api.twitch.tv/kraken/streams/sing_sing?client_id=vpmzqjo3ab8dyeslvz2ia3r3yehif3', headers=headers).json()
        streamer = json.loads(json.dumps(streamer_html))
        stream_data  = streamer['stream']
        if(stream_data == None):
            reply_message = 'Master Sing is offline'
        else:
            reply_message = 'Master Sing is live'
        await client.change_presence(game=discord.Game(name=reply_message))
        await asyncio.sleep(600) # task runs every 60 seconds

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
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
            streamer_html = requests.get('https://api.twitch.tv/kraken/streams/sing_sing?client_id=vpmzqjo3ab8dyeslvz2ia3r3yehif3', headers=headers).json()
            streamer = json.loads(json.dumps(streamer_html))
            stream_data  = streamer['stream']
            if(stream_data == None):
                reply_message = 'Master Sing is offline. FeelsBadMan'
            else:
                reply_message = 'Master Sing is live - http://www.twitch.tv/sing_sing '
                print(reply_message)
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
            
        elif message.content.startswith('!weeb'):
            reply_message = "WEEB VoHiYo THE VoHiYo NORMIES VoHiYo AWAY"
            await client.send_message(message.channel, reply_message)

        elif message.content.startswith('!koi'):
            reply_message = 'https://www.youtube.com/watch?v=gK57X6WWi5E'
            await client.send_message(message.channel, reply_message)
            
        elif message.content.startswith('!wutface'):
            reply_message = "https://cdn.discordapp.com/attachments/259440947434225664/297810508650905611/16998849_993717407439407_6365115539161661315_n.jpg"
            await client.send_message(message.channel, reply_message)

        elif message.content.startswith('!love'):
            pride = message.content[5:]
            if pride == '':
                pride = 'Windows 10 updates'
            mmr = randint(0,100)
            reply_message = 'Hey ' + str(message.author).split('#', 1)[0]
            reply_message = reply_message + ', your love for '
            reply_message = reply_message +  pride
            reply_message = reply_message + ' is around '
            reply_message = reply_message + str(mmr)
            if(mmr > 50):
                reply_message = reply_message + '%'
                if pride == 'Windows 10 updates':
                     reply_message = reply_message + ' because you didn\'t mention any name'
                     reply_message = reply_message + ' LUL'
                else:
                    reply_message = reply_message + ' KappaPride'
            else:
                reply_message = reply_message + '%'
                if pride == 'Windows 10 updates':
                    reply_message = reply_message + ' because you didn\'t mention any name'
                    reply_message = reply_message + ' LUL'
                else:
                    reply_message = reply_message + ' FeelsBadMan'
            await client.send_message(message.channel, reply_message)

        elif message.content.startswith('!uniok'):
            reply_message = 'http://i.imgur.com/HdxYRqM.png'
            await client.send_message(message.channel, reply_message)

        elif message.content.startswith('!matuslap'):
            reply_message = 'https://gfycat.com/SlightVastCottonmouth'
            await client.send_message(message.channel, reply_message)

        elif message.content.startswith('!fuccboi'):
            reply_message = 'sheep is today\'s fuccboi'
            await client.send_message(message.channel, reply_message)
            
            
        elif message.content.startswith('!mydong'):
            mmr = randint(0,25)
            reply_message = 'Hey ' + str(message.author).split('#', 1)[0]
            reply_message = reply_message + ', your dong hangs '
            reply_message = reply_message + str(mmr)
            reply_message = reply_message + ' cms low Jebaited'
            await client.send_message(message.channel, reply_message)

        elif message.content.startswith('!help'):
            reply_message = """
            ```
            
Here are a list of commands Beanchild can reply to:
!info - Check whether Singsing is live or not.
!mymmr - Check your true MMR.
!mydong - ur mum knows about it anyway haHAA
!love - KappaPride
!weeb - the normies away
!bean - FRICCIN
!wutface - weebs
        ```"""
            await client.send_message(message.channel, reply_message)

            
        elif message.content.startswith('!bean'):
            await client.send_message(message.channel, "http://i0.kym-cdn.com/photos/images/facebook/001/166/993/284.png")
        
        
client.loop.create_task(my_background_task())

client.run('Mjk2NzI2MjExODE0NjIxMTg2.C72dJw.qgiXa_FvhGX9DY-8pK3ZbzV1FwY')
