import discord
from discord.ext import commands
import music
import os


bot=commands.Bot(command_prefix = ">")
status='hi'

@bot.event
async def on_ready():
    print('Online')



@bot.command()
async def hello(ctx):
    await ctx.channel.send("Hi! " + str(ctx.author.mention))


bot.run("OTA4NTc0NzkzNDE3MjYxMDU3.YY3uNw.hmuW3WDpjZq_X9ilq4z_QkNEzmo")

