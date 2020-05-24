from ticker_bot.tickers.ticker.info import TickerInfo

from discord.ext import commands
from cogs.bot import Bot


class TickerInfoCog(Bot):
    LABEL = 'TickerInfoCog'
    def __init__(self, bot):
        super().__init__(bot)

    