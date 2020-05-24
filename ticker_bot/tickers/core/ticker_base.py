import yfinance as yf
import datetime 

from ticker_bot.tickers.core.ticker_cache_base import TickerCache


class TickerBase(TickerCache):
    NA_STRING = 'Information Unavailable'
    LABEL = 'TickerBase'
    TICKER_ATTRIBUTE = None
    TICKER_CACHE_SECONDS = 900
    def __init__(self, ticker: str):
        self._ticker = ticker.strip().upper()
        super().__init__(self.TICKER_ATTRIBUTE, self.TICKER_CACHE_SECONDS)
        
    @property
    def ticker(self):
        cache_exists, cached_ticker = self.read_file_from_cache(self._ticker)
        if cache_exists:
            return cached_ticker
        ticker = yf.Ticker(self._ticker)
        if self.TICKER_ATTRIBUTE is not None:
            try:
                ticker = getattr(ticker, self.TICKER_ATTRIBUTE)
                if hasattr(self, 'period'):
                    ticker = ticker(getattr(self, 'period'))
            except Exception:
                return None
        self.write_file_to_cache(self._ticker, ticker)
        return ticker

    def ticker_format_conversion(self, ticker):
        return ticker

    def ticker_data_from_dict(self, data_dict):
        ticker = self.ticker_format_conversion(self.ticker)
        if ticker is None:
            return [f'{self.LABEL} {self.NA_STRING} for ${self._ticker}']
        return [f'{v}: {self.data_string(ticker, k)}' for k, v in data_dict.items()]
    
    def ticker_data_from_timeseries(self, data_dict):
        ticker = self.ticker_format_conversion(self.ticker)
        if ticker is None:
            return [f'{self.LABEL} {self.NA_STRING} for ${self._ticker}']
        header = list(data_dict.keys())
        data = [header]
        for tick in ticker:
            data.append([self.data_string(tick, k) for k in data_dict.keys()])
        return data

    @classmethod
    def data_string(cls, ticker, key):
        data = ticker.get(key, cls.NA_STRING)
        if data is None:
            return cls.NA_STRING
        return cls.data_timestamp(data)

    @classmethod
    def data_timestamp(cls, data):
        if isinstance(data, datetime.datetime):
            return str(data.date())
        return data