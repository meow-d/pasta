from discord.ext import commands
import discord
from discord.utils import get
#from discord import FFmpegPCMAudio

import random
import time
from youtube_dl import YoutubeDL

import csv
# filter function for meow pasta list
def filterFunc(x):
    if x == "pastaName":
        return False
    else:
        return True

# TODO error handling

# import logging
#logging.basicConfig(level=logging.INFO)

# bot command prefix
bot = commands.Bot(command_prefix='meow ')

@bot.event
async def on_ready():
    print('connected to Discord as ' + bot.user.name)

# template
'''
@bot.command(help='')
async def echo(ctx, arg):
    await ctx.send(arg)
'''

@bot.command(help='aaaaa')
async def say(ctx,*,text):
    await ctx.send(str(text))

@bot.command(help='echoooooo ᴇᴄʜᴏᴏᴏᴏᴏᴏ ᵉᶜʰᵒᵒᵒᵒᵒᵒ')
async def echo(ctx):
    LastMessage = await ctx.history(limit=1, before=ctx.message).flatten()
    await ctx.send(LastMessage[0].content)

@bot.command(help='owo i\'ll roll a dice for you')
async def dice(ctx,faces):
    if faces == "":
        faces = 6   
    await ctx.send("you rolled a " + str(random.randrange(1,int(faces),1)))

@bot.command(help='when you\'re too lazy to even copy and paste')
async def pasta(ctx,pastaName):
    pastaCSV = csv.DictReader(open('pasta.csv', mode='r'))
    if pastaName == "list":
        embedText = discord.Embed(title='title', description='\n'.join(filter(filterFunc,pastaCSV.fieldnames)))
        await ctx.send(embed = embedText)
    else:
        try:
            for row in pastaCSV:
                pastaContent = (row[pastaName])
        except:
            pastaContent = (f"sorry i can't find {pastaName}")
        await ctx.send(pastaContent)

@bot.command(help='nut')
async def emoji(ctx): 
    await ctx.send("<:Pokimane:761513674056794112> <:lmao:761792146571264050> <a:dancin:762655521730986015> <a:dancin:762655521730986015> <a:dancin:762655521730986015> <a:dancin:762655521730986015> <a:dancin:762655521730986015> <a:dancin:762655521730986015>")

@bot.command()
async def join(ctx,link):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(bot.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(link, download=False)
        URL = info['formats'][0]['url']
        voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
    else:
        await ctx.send("Already playing song")
        return

bot.run('NzYxNzcyNzQzNTQ0Nzk5MjUy.X3feJw.TIuokEm9mRCdVVBQmHOaTGhaLBI')