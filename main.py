import discord
from discord.ext import commands
import music
import os

cogs = [music]

client = commands.Bot(command_prefix=">")
status = 'hi'


for i in range(len(cogs)):
    cogs[i].setup(client)


@client.event
async def on_ready():
    print('Online')


@client.command()
async def hello(ctx):
    await ctx.channel.send("Hi! " + str(ctx.author.mention))


client.run("OTA4NTc0NzkzNDE3MjYxMDU3.YY3uNw.hmuW3WDpjZq_X9ilq4z_QkNEzmo")
