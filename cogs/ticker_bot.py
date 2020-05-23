import yfinance as yf
from discord.ext import commands
from cogs.bot import Bot

class TickerBot(Bot):
    NA_STRING = 'N/A'
    LABEL = 'TickerBot'
    def __init__(self, bot):
        super().__init__(bot)

    @property
    def ticker(self, ctx, *, ticker: str):
        return yf.Ticker(ticker.strip().upper())


class TickerInfo(Bot):
    LABEL = 'TickerInfo'
    def __init__(self, bot):
        super().__init__(bot)

    @property
    def ticker_info_summary_keys(self):
        return ['symbol', 'shortName', 'sector', 'fullTimeEmployees', 'longBusinessSummary', 'currency']

    @property
    def ticker_info_price_keys(self):
        return ['dayHigh', 'dayLow', 'previousClose', 'regularMarketOpen']

    @property
    def ticker_info_volume_keys(self):
        return ['regularMarketVolume', 'volume24Hr', 'averageDailyVolume10Day', 'averageVolume']
    
    @property
    def ticker_info_market_keys(self):
        return ['forwardPE', 'trailingPE']