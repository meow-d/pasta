from discord.ext import commands
import discord

import csv
import time
import random
import asyncio
import keep_alive
import youtube_dl
from YTDLSource import YTDLSource
from googleapiclient.discovery import build
#import logging
#logging.basicConfig(level=logging.INFO)

import os
from dotenv import load_dotenv
load_dotenv()


# bot command prefix
bot = commands.Bot(command_prefix='meow ', case_insensitive=True)

@bot.event
async def on_ready():

    print('connected to Discord as ' + bot.user.name + '\n')


# template
'''
@bot.command(help='')
async def name(ctx, arg):

    await ctx.send(arg)
'''


@bot.command(help='ping pong ping pong ping ping pong')
async def ping(ctx):

    await ctx.send('pong')


@bot.command(help='make the bot say stupid things')
async def say(ctx,*,text):

    await ctx.send(text)


@bot.command(help='echoooooo ᴇᴄʜᴏᴏᴏᴏᴏᴏ ᵉᶜʰᵒᵒᵒᵒᵒᵒ')
async def echo(ctx):

    LastMessage = await ctx.history(limit=1, before=ctx.message).flatten()
    await ctx.send(LastMessage[0].content)


@bot.command(help='owo i\'ll roll a dice for you')
async def dice(ctx,faces=6):
    try:
        faces = int(faces)
        diceValue = random.randrange(1,faces,1)
        await ctx.send("you rolled a " + str(diceValue))
    except:
        await ctx.send(ctx.author.mention + ' state a number larger than 1 you dumb dumb')


@bot.command(help='when you\'re too lazy to even copy and paste')
async def pasta(ctx,*,pastaName):

    pastaCSV = csv.DictReader(open('bot/pasta.csv', mode='r'))
    try:
        for row in pastaCSV:
            pastaContent = (row[pastaName])
            await ctx.send(pastaContent)
    except:
        embed_pastaError = discord.Embed(description=f"sorry i can't find {pastaName}")
        message = await ctx.send(embed = embed_pastaError)
        await message.delete(3)


@bot.command(help='list of cpoypastas', aliases=['pl'])
async def pastalist(ctx):

    pastaCSV = csv.DictReader(open('bot/pasta.csv', mode='r'))
    pastaNameList = '\n'.join(pastaCSV.fieldnames[1:])
    embed_pastaList = discord.Embed(description = pastaNameList)
    await ctx.send(embed = embed_pastaList)


@bot.command(help='nut')
async def emoji(ctx): 

    await ctx.send("<:Pokimane:761513674056794112> <:lmao:761792146571264050> <a:dancin:762655521730986015> <a:dancin:762655521730986015> <a:dancin:762655521730986015> <a:dancin:762655521730986015> <a:dancin:762655521730986015> <a:dancin:762655521730986015>")


@bot.command(help='join voice channel')
async def join(ctx):

    try:
        channel = ctx.author.voice.channel
    except:
        await ctx.send(ctx.author.mention + ' connect to a voice channel first you big dumb')
    else:
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
        await channel.connect()


@bot.command(aliases=['stop','s'])
async def leave(ctx):

    await ctx.voice_client.disconnect()


@bot.command(aliases=['pf'])
async def aaaahh(ctx,filename):

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('audio files/' + filename + '.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)


async def search(query):
    youtube = build("youtube",'v3',developerKey=os.getenv('GOOGLE_API_KEY'))
    search_response = youtube.search().list(

        q=query,
        type="video",
        part="id,snippet",
        maxResults=1

    ).execute()
    return ('https://www.youtube.com/watch?v=' + search_response['items'][0]['id']['videoId'])


@bot.command(aliases=['p'])
async def play(ctx, *, query):

    try:
        channel = ctx.author.voice.channel
    except:
        await ctx.send(ctx.author.mention + ' connect to a voice channel first you big dumb')
    else:
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
        await channel.connect()

        async with ctx.typing():
            url = await search(query)
            player = await YTDLSource.from_url(url, loop=ctx.bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

        embed_player = discord.Embed(description=f'**Now playing:** {player.title}')
        await ctx.send(embed=embed_player)


keep_alive.keep_alive()
bot.run(os.getenv('DISCORD_TOKEN'))