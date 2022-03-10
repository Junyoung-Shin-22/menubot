import discord
import random
import re
from menu import menulist

with open('token.txt') as f:
    token = f.read()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

p = '(\-\w \w*)'

@client.event
async def on_message(message):
    if message.channel.id == 907585718979805184: # oracle channel
        if message.content == 'ㅈㅁㅁ':
            await message.channel.send(random.choice(menulist))

client.run(token)