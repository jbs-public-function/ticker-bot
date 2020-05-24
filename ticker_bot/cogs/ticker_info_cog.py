from ticker_bot.tickers.ticker.info import TickerInfo

from discord.ext import commands
from cogs.base_cog import BaseCog


class TickerInfoCog(BaseCog):
    LABEL = 'TickerInfoCog'
    def __init__(self, bot):
        super().__init__(bot)

    @commands.command()
    async def summary(self, ctx, *, ticker):
        info = TickerInfo(ticker)
        for _info in info.ticker_info_summary():
            await ctx.send(_info)
    
    @commands.command()
    async def price(self, ctx, *, ticker):
        info = TickerInfo(ticker)
        for _info in info.ticker_info_price():
            await ctx.send(_info)
    
    @commands.command()
    async def volume(self, ctx, *, ticker):
        info = TickerInfo(ticker)
        for _info in info.ticker_info_volume():
            await ctx.send(_info)

    @commands.command()
    async def pe(self, ctx, *, ticker):
        info = TickerInfo(ticker)
        for _info in info.ticker_info_pe():
            await ctx.send(_info)
