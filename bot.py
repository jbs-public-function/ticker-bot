import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
import discord
from discord.ext import commands


client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    logger.info('Bot is ready.')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')


@client.command(aliases=['8ball', 'test'])
async def _eight_ball(ctx, *, question):
    import random
    responses = ['a1', 'b2', 'c3']
    await ctx.send(f'Question: {question}\nMagic 8ball Says: {random.choice(responses)}')


client_token = 'NzEzODA5NDE2MDYzMDI1MTgz.Xsl8JA.jWAJjyf8FqicGSumjzUil9rDoyU'
client.run(client_token)