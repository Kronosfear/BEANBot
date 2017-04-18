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
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
from queue import *
import youtube_dl

client = discord.Client()

#video_queue = queue.Queue()




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
            print(message.author)
            if str(message.author) == 'HERE I AM - Puck 2016#5286':
                reply_message = "You are not allowed to use this command you fake weeb"
            else:
                reply_message = "WEEB VoHiYo THE VoHiYo NORMIES VoHiYo AWAY"
            await client.send_message(message.channel, reply_message)


 #-------------------------------------------------KOI------------------------------------------------------


        elif message.content.startswith('!koi'):
            reply_message = 'https://www.youtube.com/watch?v=gK57X6WWi5E'
            await client.send_message(message.channel, reply_message)



#----------------------------------------------VLECXIUS----------------------------------------------------

        elif message.content.startswith('!vlecxius'):
            await client.send_file(message.channel, 'images/vlecxius.png')


#------------------------------------------------BANE---------------------------------------------------

        elif message.content.startswith('!bane'):
            reply_message = 'http://www.operatorchan.org/pasta/src/140106838095.gif'
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


#--------------------------------------------CULTURE----------------------------------------------------------

        elif message.content.startswith('!culture'):
            reply_message = 'https://cdn.discordapp.com/attachments/292869746293211146/303203330874671105/FB_IMG_1492359657145.jpg'
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


#------------------------------------------EXPLOSION----------------------------------------------------

        elif message.content.startswith('!explosion'):
            grill_list = ['https://cdn.discordapp.com/attachments/259440947434225664/299169011030294529/17759703_1225066617591719_652388841780661578_n.jpg',
                                      'https://cdn.discordapp.com/attachments/259440947434225664/299169012317814784/299442.jpg',
                                      'https://cdn.discordapp.com/attachments/259440947434225664/299169014222028810/17795722_10212222788942910_508290901603216617_n.jpg',
                                      'https://cdn.discordapp.com/attachments/259440947434225664/299169016201871360/17796264_1133601226748505_2122562440588666354_n.jpg',
                                      'https://cdn.discordapp.com/attachments/259440947434225664/299169017426477056/17760916_1396122297114761_6981183599349534997_o.jpg',
                                      'https://cdn.discordapp.com/attachments/259440947434225664/299169021318660108/CcmCfJuW8AAtsw8.jpg',
                                      'https://cdn.discordapp.com/attachments/259440947434225664/299169032479703040/flat1000x1000075f.u5.jpg',
                                      'https://cdn.discordapp.com/attachments/259440947434225664/299169034937696266/2HoYcaN.png',
                                      'https://cdn.discordapp.com/attachments/259440947434225664/299169039148646400/Megumin_main_image.png',
                                      'https://cdn.discordapp.com/attachments/259440947434225664/299169053958733825/Konosuba-1.jpg',
                                      'https://cdn.discordapp.com/attachments/259440947434225664/299169075505135626/687474703a2f2f34352e6d656469612e74756d626c722e636f6d2f3166646564303566323938626661646437626633623363.gif',
                                      'https://cdn.discordapp.com/attachments/259440947434225664/299169075760857088/nICa2zf.jpg',
                                      'https://cdn.discordapp.com/attachments/259440947434225664/299169085286252544/wQL7geT.jpg',
                                      'https://cdn.discordapp.com/attachments/259440947434225664/299169092735205386/tumblr_o2ejc7yXPF1s21xzoo1_500.gif',
                                      'https://cdn.discordapp.com/attachments/259440947434225664/299169109202173952/fg6nRds.png',
                                      'https://cdn.discordapp.com/attachments/292869746293211146/303203627697176607/eJwFwUEOgyAQAMC_8ADWBbK43pqe7c30TJCgiQpl8dT07535qrsdalJb71UmgHWXWNqqpZcWctK5lHykUHfRsZwQeg9xO9PVBQyb.png'
                                    ]
            random.shuffle(grill_list)
            reply_message = grill_list[0]
            await client.send_message(message.channel, reply_message)

            
#------------------------------------------SMUG----------------------------------------------------

        elif message.content.startswith('!smug'):
            smug_list = ['https://cdn.discordapp.com/attachments/299190496964771841/299191233245478913/1459243739540.jpg',
                                      'https://cdn.discordapp.com/attachments/299190496964771841/299191240052965376/1444236147368.png',
                                      'https://cdn.discordapp.com/attachments/299190496964771841/299191248886038529/1436640383591-3.png',
                                      'https://cdn.discordapp.com/attachments/299190496964771841/299191250861555712/1436640383572-0.jpg',
                                      'https://cdn.discordapp.com/attachments/299190496964771841/299191287456727043/1376763247995.png',
                                      'https://cdn.discordapp.com/attachments/299190496964771841/299191291697299458/1371730299235.png',
                                      'http://i.imgur.com/Dd7bbcQ.png',
                                      'http://i.imgur.com/c1zbwwq.png',
                                      'http://i.imgur.com/yS8IvBG.png',
                                      'http://i.imgur.com/WcC6Poc.png',
                                      'http://i.imgur.com/POQWJow.png',
                                      'http://i.imgur.com/sh5YFcJ.png',
                                      'http://i.imgur.com/1pwotJC.png',
                                      'http://i.imgur.com/aWNzx6z.png',
                                      'https://cdn.discordapp.com/attachments/292869746293211146/300994617619513356/1471581644134.png',
                                      'http://i.imgur.com/JJhi5NP.jpg',
                                    ]
            random.shuffle(smug_list)
            print(message.author)
            if str(message.author) == 'koi#9765':
                reply_message = 'http://i.imgur.com/gyZB2Bo.jpg'
            else:
                reply_message = smug_list[0]
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
            em = discord.Embed(title='', description=reply_message, colour=0x008A00)
            em.set_author(name='BEANBot', icon_url=client.user.default_avatar_url)
            await client.send_message(message.channel, embed=em)





 #----------------------------------------------FUCCBOI-------------------------------------------------------


 

        elif message.content.startswith('!fuccboi'):
            reply_message = 'sheep is today\'s fuccboi'
            await client.send_message(message.channel, reply_message)




#--------------------------------------------------VEIN----------------------------------------------------




        elif message.content.startswith('!vein'):
            await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/259440947434225664/302481919076073474/ezgif-1-11cf8dd748.gif")


            
            
#------------------------------------------------MYDONG------------------------------------------------------




        elif message.content.startswith('!mydong'):
            mmr = randint(0,25)
            reply_message = 'Hey ' + str(message.author).split('#', 1)[0]
            reply_message = reply_message + ', your dong hangs '
            reply_message = reply_message + str(mmr)
            reply_message = reply_message + ' cms low Jebaited'
            await client.send_message(message.channel, reply_message)




#------------------------------------------------MYLOVE------------------------------------------------------



        elif message.content.startswith('!mylove'):
            reply_message = 'Hey ' + str(message.author).split('#', 1)[0]
            reply_message = reply_message + ' your true love is '
            server = client.get_server('292869746293211146')
            memb = [x for x in server.members]
            random.shuffle(memb)
            mem = memb[0]
            if mem.nick == None:
                    reply_message = reply_message + str(mem).split('#', 1)[0]
            else:
                    reply_message = reply_message + str(mem.nick).split('#', 1)[0]
            await client.send_message(message.channel, reply_message)

            


#----------------------------------------------THINKING------------------------------------------------------




        elif message.content.startswith('!thinking'):
            reply_message = 'https://cdn.discordapp.com/attachments/292869746293211146/300253029389565952/a9ef568c4c133ad983e836b5bcb90bcae68feb3190df7e37aa51958678c94134.png'
            await client.send_message(message.channel, reply_message)

            


#-----------------------------------------------DAISUKI-----------------------------------------------------


        elif message.content.startswith('!daisuki'):
            await client.send_file(message.channel, 'images/daisuki.jpg')


#----------------------------------------------SMORC------------------------------------------------------

        elif message.content.startswith('!smorc'):
            await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/292869746293211146/300989271316365312/IMG_27042016_140301.png")


#------------------------------------------------HELP-----------------------------------------------------

        elif message.content.startswith('!help'):
            reply_message = """
            
!info - Check whether Singsing is live or not

!streams - Top 5 Streams

!mymmr - Check your true MMR.

!mydong - ur mum knows about it anyway haHAA

!love - KappaPride

!mylove - gachiGASM

!gsearch - Google Search !gsearch <search term>

!smug - Eyy

!weeb - the normies away

!bean - FRICCIN

!bane - Dr. Pavel, I'm CIA

!vein - BANE?

!wutface - weebs

!vlecxius - who

!grill - Kreygasm

!matuslap - dat ass

!thinking - Not :thonking:

!uniok - Marry me universe

!explosion - EKSUPUROOSHUN

!fuccboi - who could it be :thinking:

!smorc - Hey I have an idea.

!culture - Ah I see



        """
            em = discord.Embed(title='Here are the commands Beanchild can reply to', description=reply_message, colour=0x008A00)
            em.set_author(name='BEANBot', icon_url=client.user.default_avatar_url)
            await client.send_message(message.channel, embed=em)

 #-------------------------------------------------BEAN----------------------------------------------------------

 
        elif message.content.startswith('!bean'):
            await client.send_message(message.channel, "http://i0.kym-cdn.com/photos/images/facebook/001/166/993/284.png")


#*************************************************************************************************************************


#-----------------------------------------YOUTUBE STUFF---------------------------------------------------------

        elif message.content.startswith('!play'):
            searchtext = message.content[6:]
            query = urllib.parse.quote(searchtext)
            url = "https://www.youtube.com/results?search_query=" + query
            response = urllib.request.urlopen(url)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            vid  = soup.findAll(attrs={'class':'yt-uix-tile-link'})[0]
            reply_message = 'Currently playing ' + vid['title']
            await client.send_message(message.channel, reply_message)
            voice = await client.join_voice_channel(message.author.voice_channel)
            video_url = 'http://www.youtube.com' + vid['href']
            player = await voice.create_ytdl_player(video_url)
            player.start()

client.loop.create_task(my_background_task())


client.run('Mjk2NzI2MjExODE0NjIxMTg2.C72dJw.qgiXa_FvhGX9DY-8pK3ZbzV1FwY')
