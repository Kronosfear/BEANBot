import discord
import asyncio
from twitch.api import v3 as twitch
from twitch.exceptions import ResourceUnavailableException
from random import randint



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
            stream_data = twitch.channels.by_name('sing_sing')['status']
            if(stream_data == None):
                reply_message = 'Master Sing is offline. FeelsBadMan'
            else:
                reply_message = 'Master Sing is live - ' + stream_data
            await client.send_message(message.channel, reply_message)
        elif message.content.startswith('!mymmr'):
            mmr = randint(0,9999)
            reply_message = message.author + '\'s MMR is ' + str(mmr) + '!'
            await client.send_message(message.channel, reply_message)
        elif message.content.startswith('!mydong'):
            mmr = randint(0,25)
            reply_message = message.author + '\'s dong hangs ' + str(mmr) + ' cm low. Jebaited'
            await client.send_message(message.channel, reply_message)
        
        
client.run('Mjk2NzI2MjExODE0NjIxMTg2.C72dJw.qgiXa_FvhGX9DY-8pK3ZbzV1FwY')
