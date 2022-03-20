from http import client
import discord
import random

# 1. Discord Bot main Token
TOKEN='PASTE YOUR TOKEN HERE'

# 2. Install pip using Teriminal code: "pip install discord"

# 3. Imports-discord and random
    # When import discord give some error, Refer: https://stackoverflow.com/questions/66610678/import-discord-could-not-be-resolved
    # Solution: The solution is to change the Python Interpreter. You can do it by Ctrl+Shift+P and choose "Python: Select Interpreter" in visual studio code.

# 4. Code
client=discord.Client()
@client.event
async def on_ready():
    print('We are Login as {0.user}'.format(client))

@client.event
async def on_message(message):
    # assign varibles
    username=str(message.author).split('#')[0]
    user_message=str(message.content)
    channel_name=str(message.channel.name)
    bot_username=str(client.user).split('#')[0]
    # console log
    print(f'{username}: "{user_message}" in {channel_name} chat !')
    # Decline responce: for duplicate message(Bot message) 
    if message.author==client.user:
        return
    # user message: responce as per request
    if message.channel.name=='general':
        if user_message.lower()=='hi':
            await message.channel.send(f'Hi {username}!, I am {client.user}')
            return
        elif message.content.lower()=='hello':
            await message.channel.send(f'Hello {username}!, I am {bot_username}')
            return
# client runner: The client runner should only be at the end
client.run(TOKEN)