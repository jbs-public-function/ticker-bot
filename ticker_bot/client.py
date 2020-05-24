import os
import logging

from ticker_bot.cogs import ticker_info_cog, ticker_history_cog, ticker_calendar_cog

import discord
from discord.ext import commands


def client():
    client = commands.Bot(command_prefix='$')


    @client.command()
    async def load(ctx, extension):
        client.load_extension(f'cogs.{extension}')


    @client.command()
    async def unload(ctx, extension):
        client.unload_extension(f'cogs.{extension}')


    client.add_cog(ticker_info_cog.TickerInfoCog(client))
    client.add_cog(ticker_history_cog.TickerHistoryCog(client))
    client.add_cog(ticker_calendar_cog.TickerCalendarCog(client))

    client_token = os.environ.get('CLIENT_TOKEN')
    client.run(client_token)


if __name__ == '__main__':
    import time
    exception_count = 3
    exceptions = []
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('__main__')
    while True:
        try:
            logger.info('Client is starting')
            client()
        except Exception as exc:
            logger.error(exc)
            logger.info('Client is sleeping 7 minutes')
            time.sleep(450)
            exceptions.append(exc)
            if len(exceptions) == exception_count:
                raise Exception(exceptions)
        