from pandas_market_calendars.market_calendar import MarketCalendar
from datetime import datetime

class ParisStockExchangeCalendar(MarketCalendar):
    """
    Trading calendar for the Paris Stock Exchange
    """
    def __init__(self, start_date=None, end_date=None, side=None):
        super(ParisStockExchangeCalendar, self).__init__(
            start_date=start_date,
            end_date=end_date,
            side=side,
        )

    @property
    def name(self):
        return "XPAR"

    @property
    def tz(self):
        return "Europe/Paris"

    @property
    def regular_holidays(self):
        # List the regular holidays observed by the Paris Stock Exchange
        # Example: New Year's Day
        return [
            datetime(year, 1, 1) for year in range(2000, 2100)
        ]