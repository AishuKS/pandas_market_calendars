import pandas as pd
from pandas_market_calendars.market_calendar import MarketCalendar

class ISEExchangeCalendar(MarketCalendar):
    @property
    def name(self):
        return "XMAD"

    @property
    def tz(self):
        return "Europe/Madrid"

    @property
    def open_time(self):
        return pd.to_datetime('09:30:00', format='%H:%M:%S')

    @property
    def close_time(self):
        return pd.to_datetime('17:30:00', format='%H:%M:%S')

    def day_is_trading_day(self, date):
        """Check if a day is a trading day"""
        # Your logic to determine if a day is a trading day goes here.
        # This example assumes all days except for Saturdays and Sundays are trading days.
        return date.weekday() < 5
    
    def regular_holidays(self, start, end):
        return pd.date_range(start=start, end=end, freq='Y', tz=self.tz, 
                             holidays=['New Years Day',
                                       'Good Friday',
                                       '1 May (Labour Day)',
                                       'Constitution Day',
                                       'Assumption Day',
                                       'All Saints Day',
                                       'Constitution Day (Bicentenary)',
                                       'Immaculate Conception',
                                       'Christmas'])
    def is_business_day(self, date):
            return date in self.schedule(start_date=date, end_date=date)

# Now you can use the custom calendar
calendar = ISEExchangeCalendar()
print(calendar.day) # 2022-01-01