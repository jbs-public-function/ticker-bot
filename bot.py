# from core.bot import Bot

import discord
from discord.ext import commands


client = commands.Bot(command_prefix='$')
# client.add_cog(Bot(client))
@client.event
async def on_ready():
    print('Bot is ready.')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')


@client.command(aliases=['8ball', 'test'])
async def _eight_ball(ctx, *, question):
    import random
    responses = ['a1', 'b2', 'c3']
    await ctx.send(f'Question: {question}\nMagic 8ball Says: {random.choice(responses)}')

import os
client_token = os.environ.get('CLIENT_TOKEN')
client.run(client_token)