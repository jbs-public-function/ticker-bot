import yfinance as yf


class TickerBase(object):
    NA_STRING = 'N/A'
    def __init__(self, ticker=None):
        self._ticker = ticker
        
    @property
    def ticker(self) -> yf.Ticker:
        if self._ticker is None:
            raise TypeError('ticker is None')
        return self._ticker

    @ticker.setter
    def ticker(self, ticker: str):
        if not isinstance(ticker, str):
            raise AttributeError(f'Invalid ticker {ticker} with type {type(ticker)}.\nTicker must be a string.')
        self._ticker = yf.Ticker(ticker.strip().upper())


    