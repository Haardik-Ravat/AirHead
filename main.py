import discord
from discord.ext import commands
import music
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('>'):
        await message.channel.send('Hello!')



client.run("OTA4NTc0NzkzNDE3MjYxMDU3.YY3uNw.hmuW3WDpjZq_X9ilq4z_QkNEzmo")

