from ticker_bot.tickers.core.ticker_base import TickerBase


class TickerCalendar(TickerBase):
    LABEL = 'TickerCalendar'
    TICKER_ATTRIBUTE = 'calendar'
    TICKER_CACHE_SECONDS = 86400
    def __init__(self, ticker):
        super().__init__(ticker)

    def ticker_calendar_earnings(self):
        return self.ticker_data_from_dict(self.ticker_calendar_earnings_keys)

    @property
    def ticker_calendar_earnings_keys(self):
        return {'Earnings Date': 'Upcoming Earnings Call',}

    def ticker_format_conversion(self, ticker):
        if ticker is None or len(ticker.to_dict()) == 0:
            return None
        max_key = max(ticker.to_dict().keys())
        return ticker.to_dict()[max_key]
