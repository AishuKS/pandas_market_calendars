from pandas_market_calendars.market_calendar import MarketCalendar
import pandas as pd


class PolandStockExchange(MarketCalendar):
    """
    Implementation of the WSE (Warsaw Stock Exchange) calendar.
    """
    # Trading hours and holidays for the WSE are not specified. 
    # Assuming the same hours as for the NASDAQ.
    @property
    def name(self):
        return "XWAR"

    @property
    def tz(self):
        return "Europe/Warsaw"

    @property
    def open_time(self):
        return pd.to_datetime("10:00:00", format="%H:%M:%S")

    @property
    def close_time(self):
        return pd.to_datetime("17:00:00", format="%H:%M:%S")

    @property
    def regular_holidays(self):
        # Source: https://www.nasdaqtrader.com/trader.aspx?id=CalendarModule
        # The following regular holidays are observed by the WSE:
        return [
            "2021-01-01", # New Year's Day
            "2021-01-06", # Epiphany
            "2021-04-02", # Good Friday
            "2021-04-05", # Easter Monday
            "2021-05-01", # Labour Day
            "2021-05-03", # Constitution Day
            "2021-05-31", # Corpus Christi
            "2021-06-23", # Wednesday before Pentecost
            "2021-06-24", # Feast of John the Baptist
            "2021-08-15", # Assumption of the Blessed Virgin Mary
            "2021-11-01", # All Saints' Day
            "2021-11-11", # Independence Day
            "2021-12-25", # Christmas Day
            "2021-12-26", # Boxing Day
        ]

    @property
    def adhoc_holidays(self):
        # No ad hoc holidays specified.
        return []