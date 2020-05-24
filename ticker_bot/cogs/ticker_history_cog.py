from ticker_bot.tickers.ticker.price_history import TickerPriceHistory

from discord.ext import commands
from cogs.base_cog import BaseCog


class TickerHistoryCog(BaseCog):
    LABEL = 'TickerHistoryCog'
    def __init__(self, bot):
        super().__init__(bot)

    @commands.command(aliases=['price-history', '7day', 'weekly', 'week', 'hist'])
    async def history(self, ctx, *, ticker):
        history = TickerPriceHistory(ticker)
        await ctx.send(f'7 Day Price History for ${ticker}')
        for hist in self.format_table(history.ticker_one_week_price_history()):
            await ctx.send(hist)
