import discord
import random

from menu import *
from parser import *

with open('token.txt') as f:
    TOKEN = f.read()

CHANNEL_ID = 555288184657936385 # 오늘-뭐-먹지

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return
    
    if message.channel.id != CHANNEL_ID:
        return

    content = message.content
    if not content:
        return
    
    command, *args = content.split()

    if command != 'ㅈㅁㅁ':
        return
    
    parsed_args = PARSER.parse_args(args)
    
    if parsed_args is None:
        content = f'''
        {message.author.mention}
        ```{PARSER_HELP}```
        '''
        await message.channel.send(content)
        return
    
    category = parsed_args.category
    amount = parsed_args.amount

    if amount > 10:
        amount = 10
    elif amount < 1:
        amount = 1

    menus = '\n'.join(random.choices(MENU_LIST[category], k=amount))
    content = f'''
        {message.author.mention}
        ```{menus}```
        '''
    await message.channel.send(content)

if __name__ == '__main__':
    client.run(TOKEN)