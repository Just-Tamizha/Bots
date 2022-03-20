from http import client
import discord
import random

# 1. Discord Bot main Token
TOKEN='OTUzMTI3NjcyNTM4NjExNzYy.YjADUQ.eXySKO8YL8S-1_necNZXlcPzKqo'

# 2. Install pip using Teriminal code: "pip install discord"

# 3. Imports-discord and random

# 4. Code
client=discord.Client()
@client.event
async def on_ready():
    print('We are Logged as {0.user}'.format(client))
client.run(TOKEN)
