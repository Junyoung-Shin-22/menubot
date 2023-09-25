import discord
import random

from menu import *

with open('./txt/token.txt') as f:
    TOKEN = f.read()

with open('./txt/channels.txt') as f:
    CHANNELS = [int(x) for x in f.read().splitlines()]

intents = discord.Intents.all()
BOT = discord.Client(intents=intents)

@BOT.event
async def on_ready():
    print(f'{BOT.user} is ready')

@BOT.event
async def on_message(message):
    return_cond = [
        message.author.bot == True,
        message.author.id == BOT.user.id,
        message.channel.id not in CHANNELS,
    ]

    content = message.content
    if not content:
        return
    
    if content == 'ㅈㅁㅁ':
        menu = get_menu()
        if menu is None:
            menu = '굶어'
        
        await message.channel.send(menu)