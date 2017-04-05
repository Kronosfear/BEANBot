import discord
import asyncio
from twitch.api import v3 as twitch
from twitch.exceptions import ResourceUnavailableException
from random import randint
import argparse
import requests
import json
import random
from google import google

client = discord.Client()

#*************************************************************************************************************************



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
        await asyncio.sleep(60) # task runs every 60 seconds


#*************************************************************************************************************************



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    
#*****************************************************INFO****************************************************************


@client.event
async def on_message(message):
    if message.author != 'BEANBot#8947':
        if message.content.startswith('!info'):
            streamer = None
            if len(message.content) == 5:
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
                streamer_html = requests.get('https://api.twitch.tv/kraken/streams/sing_sing?client_id=vpmzqjo3ab8dyeslvz2ia3r3yehif3', headers=headers).json()
                streamer = json.loads(json.dumps(streamer_html))
                stream_data  = streamer['stream']
                if(stream_data == None):
                    reply_message = 'Master Sing is offline. FeelsBadMan'
                else:
                    reply_message = 'Master Sing is live - http://www.twitch.tv/sing_sing '
                    print(reply_message)

                    
            else:
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
                url = 'https://api.twitch.tv/kraken/streams/'
                url = url + message.content[6:]
                url= url + '?client_id=vpmzqjo3ab8dyeslvz2ia3r3yehif3'
                streamer_html = requests.get(url, headers=headers).json()
                streamer = json.loads(json.dumps(streamer_html))
                if streamer == None:
                    reply_message = 'No such stream found'
                else:
                    stream_data  = streamer['stream']
                    reply_message = 'http://www.twitch.tv/'
                    if stream_data == None:
                        reply_message += message.content[6:]
                        reply_message += ' is offline'
                    else:
                        reply_message += message.content[6:]
                        reply_message += ' is live'

            await client.send_message(message.channel, reply_message)

            
#----------------------------------------------------STREAMS----------------------------------------------
 

        elif message.content.startswith('!streams'):
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
            streamer_html = requests.get('https://api.twitch.tv/kraken/streams?game=Dota%202&client_id=vpmzqjo3ab8dyeslvz2ia3r3yehif3&language=en', headers=headers).json()
            streamer = json.loads(json.dumps(streamer_html))
            stream_data = streamer['streams']
            i = 1
            reply_message = """
            Top 5 Dota streams:\n"""
            for stream in stream_data[:5]:
                print (json.dumps(stream, indent = 4))
                name = stream['channel']['display_name']
                url = "https://www.twitch.tv/" + stream['channel']['name']
                reply_message = reply_message + str(i)
                reply_message = reply_message + ". "
                reply_message = reply_message + name
                reply_message = reply_message + " - <"
                reply_message = reply_message + url
                reply_message = reply_message + ">\n"
                i+=1
            await client.send_message(message.channel, reply_message)


            
#-----------------------------------------------MYMMR------------------------------------------------------

        elif message.content.startswith('!mymmr'):
            mmr = randint(0,9999)
            reply_message = 'Hey ' + str(message.author).split('#', 1)[0]
            reply_message = reply_message + ', your MMR is ' + str(mmr)
            if  mmr > 5999:
                reply_message = reply_message + ' PogChamp'
            else:
                reply_message = reply_message + ' LUL'
            await client.send_message(message.channel, reply_message)

 #-----------------------------------------------WEEB------------------------------------------------------

            
        elif message.content.startswith('!weeb'):
            if message.author != 'HERE I AM - Puck 2016#5286':
                reply_message "You are not allowed to use this command you fake weeb"
            else:
                reply_message = "WEEB VoHiYo THE VoHiYo NORMIES VoHiYo AWAY"
            await client.send_message(message.channel, reply_message)


 #-------------------------------------------------KOI------------------------------------------------------


        elif message.content.startswith('!koi'):
            reply_message = 'https://www.youtube.com/watch?v=gK57X6WWi5E'
            await client.send_message(message.channel, reply_message)

 #-----------------------------------------------WUTFACE--------------------------------------------------

            
        elif message.content.startswith('!wutface'):
            reply_message = "https://cdn.discordapp.com/attachments/259440947434225664/297810508650905611/16998849_993717407439407_6365115539161661315_n.jpg"
            await client.send_message(message.channel, reply_message)

 #--------------------------------------------LOVE-----------------------------------------------------------

        elif message.content.startswith('!love'):
            pride = message.content[6:]
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

            
 #-------------------------------------------UNIOK-----------------------------------------------------------


        elif message.content.startswith('!uniok'):
            reply_message = 'http://i.imgur.com/HdxYRqM.png'
            await client.send_message(message.channel, reply_message)


 #--------------------------------------------MATUSLAP----------------------------------------------------------            

        elif message.content.startswith('!matuslap'):
            reply_message = 'https://gfycat.com/SlightVastCottonmouth'
            await client.send_message(message.channel, reply_message)

 #---------------------------------------------GRILL--------------------------------------------------------


        elif message.content.startswith('!grill'):
            grill_list = ['https://b.catgirlsare.sexy/aXbo.png',
                                      'https://cdn.discordapp.com/attachments/259440947434225664/298268447479955458/matu.jpg',
                                      'https://i.imgur.com/uVVvtEm.jpg',
                                      'https://pbs.twimg.com/media/CgP1ps8WEAAMuMp.jpg',
                                      'https://cdn.discordapp.com/attachments/259440947434225664/299105853955637248/Screenshot_from_2017-04-05_14-29-21.png',
                                      'https://pbs.twimg.com/media/CLkmgJ6WsAApMxz.jpg'
                                    ]
            random.shuffle(grill_list)
            reply_message = grill_list[0]
            await client.send_message(message.channel, reply_message)


 #----------------------------------------------GSEARCH------------------------------------------------------

        elif message.content.startswith('!gsearch'):
            query = message.content[9:]
            search_results = google.search(query, 1)
            reply_message = "Hey "
            reply_message = reply_message + str(message.author).split('#', 1)[0]
            reply_message = reply_message + ", here are the top results for your search: **" + query
            reply_message = reply_message + "**\n\n"
            for i in range(0,3):
                j = i + 1
                reply_message = reply_message + str(j)
                reply_message = reply_message + ". "
                reply_message = reply_message + search_results[i].name
                reply_message = reply_message + " - <"
                reply_message = reply_message + search_results[i].link
                reply_message = reply_message + ">\n"
                reply_message = reply_message + search_results[i].description
                reply_message = reply_message + "\n\n"
            await client.send_message(message.channel, reply_message)

 #----------------------------------------------FUCCBOI-------------------------------------------------------

 
            
        elif message.content.startswith('!fuccboi'):
            reply_message = 'sheep is today\'s fuccboi'
            await client.send_message(message.channel, reply_message)

            
            
#------------------------------------------------MYDONG------------------------------------------------------

        elif message.content.startswith('!mydong'):
            mmr = randint(0,25)
            reply_message = 'Hey ' + str(message.author).split('#', 1)[0]
            reply_message = reply_message + ', your dong hangs '
            reply_message = reply_message + str(mmr)
            reply_message = reply_message + ' cms low Jebaited'
            await client.send_message(message.channel, reply_message)


#----------------------------------------------THINKING------------------------------------------------------

        elif message.content.startswith('!thinking'):
            reply_message = 'https://cdn.discordapp.com/attachments/259440947434225664/298337030600130592/L5W7sIB.jpg'
            await client.send_message(message.channel, reply_message)


#------------------------------------------------HELP-----------------------------------------------------

        elif message.content.startswith('!help'):
            reply_message = """
            ```
            
Here are a list of commands Beanchild can reply to:
!info - Check whether Singsing is live or not
!streams - Top 5 Streams
!mymmr - Check your true MMR.
!mydong - ur mum knows about it anyway haHAA
!love - KappaPride
!weeb - the normies away
!bean - FRICCIN
!wutface - weebs
!grill - Kreygasm
!matuslap - dat ass
!thinking - Not :thonking:
!uniok - Marry me universe
        ```"""
            await client.send_message(message.channel, reply_message)

 #-------------------------------------------------BEAN----------------------------------------------------------

 
        elif message.content.startswith('!bean'):
            await client.send_message(message.channel, "http://i0.kym-cdn.com/photos/images/facebook/001/166/993/284.png")
        


#*************************************************************************************************************************



        
client.loop.create_task(my_background_task())
client.run('Mjk2NzI2MjExODE0NjIxMTg2.C72dJw.qgiXa_FvhGX9DY-8pK3ZbzV1FwY')
