from discord.ext import commands

import random

import csv

# TODO error handling, echo last message

# import logging
#logging.basicConfig(level=logging.INFO)

# bot command prefix
bot = commands.Bot(command_prefix='meow ')

@bot.event
async def on_ready():
    print('connected to Discord as ' + bot.user.name)

# templete
#@bot.command(help='')
#async def echo(ctx, arg):
#    await ctx.send(arg)

@bot.command(help='echoooooo ᴇᴄʜᴏᴏᴏᴏᴏᴏ ᵉᶜʰᵒᵒᵒᵒᵒᵒ')
async def echo(ctx,*,text):
    await ctx.send(str(text))

@bot.command(help='owo i\'ll roll a dice for you')
async def dice(ctx,faces):
    if faces == "":
        await ctx.send("you rolled a " + str(random.randrange(1,6,1)))
    else:
        await ctx.send("you rolled a " + str(random.randrange(1,int(faces),1)))

@bot.command(help='when you\'re too lazy to even copy and paste')
async def pasta(ctx,pastaName):
    pastaDict = csv.DictReader(open('pasta.csv', mode='r'))
    if pastaName == list:
        for row  in pastaDict:
            await ctx.send(row[pastaName])
    for row in pastaDict:
        await ctx.send(row[pastaName])

@bot.command(help='nut')
async def emoji(ctx):
    await ctx.send("<:Pokimane:761513674056794112> <:lmao:761792146571264050> <a:dancin:762655521730986015> <a:dancin:762655521730986015> <a:dancin:762655521730986015> <a:dancin:762655521730986015> <a:dancin:762655521730986015> <a:dancin:762655521730986015>")

bot.run('NzYxNzcyNzQzNTQ0Nzk5MjUy.X3feJw.TIuokEm9mRCdVVBQmHOaTGhaLBI')