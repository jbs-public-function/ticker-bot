import yfinance as yf


class TickerBot:
    def __init__(self, ticker, period=None):
        self._ticker = ticker
        self._period = period

    @property
    def ticker(self):
        return yf.Ticker(self._ticker)