# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands

TOKEN = 'NDY1MDkxMTg2MTU2MzcxOTcz.DiIeaw.1BnHH8BCihglv9XZqF7vz-77ZzE'
BOT_PREFIX = ("?")

client = Bot(command_prefix=BOT_PREFIX)

@client.command()
async def best_teammate():
    await client.say("WILN1S")

@client.command()
async def ping():
    await client.say("pong")

@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
sadsadasd
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(60)

client.run(TOKEN)
client.loop.create_task(list_servers())
