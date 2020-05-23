import discord
from discord.ext import commands


client = commands.Bot(command_prefix='$')


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


from ticker_bot.cogs import bot, ticker_bot

client.add_cog(bot.Bot(client))
client.add_cog(ticker_bot.TickerBot(client))

import os
client_token = os.environ.get('CLIENT_TOKEN')
client.run(client_token)