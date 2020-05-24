from ticker_bot.tickers.core.ticker_base import TickerBase


class TickerPriceHistory(TickerBase):
    
    LABEL = 'TickerPriceHistory'
    TICKER_ATTRIBUTE = 'history'
    
    def __init__(self, ticker):
        super().__init__(ticker)
        self.period = '7D'

    def ticker_one_week_price_history(self):
        return self.ticker_data_from_timeseries(self.ticker_price_history_keys)

    @property
    def ticker_price_history_keys(self):
        return {'Date':'Date', 'High':'High', 'Low':'Low','Open':'Open', 'Close':'Close'}

    def ticker_format_conversion(self, ticker):
        if ticker is None or len(ticker) == 0:
            return None
        ticker = ticker.reset_index().to_dict('records')
        ticker.reverse()
        return ticker