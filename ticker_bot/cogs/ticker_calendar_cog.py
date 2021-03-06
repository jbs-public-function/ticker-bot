from ticker_bot.tickers.ticker.calendar import TickerCalendar

from discord.ext import commands
from cogs.base_cog import BaseCog


class TickerCalendarCog(BaseCog):
    LABEL = 'TickerCalendarCog'
    def __init__(self, bot):
        super().__init__(bot)

    @commands.command(aliases=['earning', 'calendar'])
    async def earnings(self, ctx, *, ticker):
        calendar = TickerCalendar(ticker)
        await ctx.send(f'Upcoming Earnings for ${ticker.upper()}')
        for calendar in calendar.ticker_calendar_earnings():
            await ctx.send(calendar)
