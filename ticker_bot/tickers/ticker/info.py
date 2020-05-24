from ticker_bot.tickers.core.ticker_base import TickerBase


class TickerInfo(TickerBase):
    LABEL = 'TickerInfo'
    TICKER_ATTRIBUTE = 'info'
    TICKER_CACHE_SECONDS = 86400
    def __init__(self, ticker):
        super().__init__(ticker)

    def ticker_info_summary(self):
        return self.ticker_data_from_dict(self.ticker_info_summary_keys)

    def ticker_info_price(self):
        return self.ticker_data_from_dict(self.ticker_info_price_keys)

    def ticker_info_volume(self):
        return self.ticker_data_from_dict(self.ticker_info_volume_keys)

    def ticker_info_pe(self):
        return self.ticker_data_from_dict(self.ticker_info_market_keys)
    
    @property
    def ticker_info_summary_keys(self):
        return dict(
            symbol='Symbol', 
            shortName='Name', 
            sector='Sector', 
            marketCap='Market Cap',
            fullTimeEmployees='Full Time Employees', 
            longBusinessSummary='Summary', 
            currency='Denominated in'
            )

    @property
    def ticker_info_price_keys(self):
        return dict(
            dayHigh='Daily High',
            dayLow='Daily Low',
            previousClose='Last Close',
            regularMarketOpen='Last Open',
            fiftyTwoWeekHigh='52 Week High',
            fiftyTwoWeekLow='52 Week Low'
            )

    @property
    def ticker_info_volume_keys(self):
        return dict(
            regularMarketVolume='Market Volume',
            averageDailyVolume10Day='10 Day Average Volume',
            averageVolume='Average Volume'
        )
    
    @property
    def ticker_info_market_keys(self):
        return dict(forwardPE='Forward PE', trailingPE='Trailing PE', pegRatio='PEG Ratio')
