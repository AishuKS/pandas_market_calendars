from pandas_market_calendars.market_calendar import MarketCalendar
import pandas as pd


class SingaporeExchangeCalendar(MarketCalendar):
    """
    Implementation of the SGX (Singapore Exchange) calendar.
    """

    # Open and close times are not specified by the SGX. 
    # Assuming the same hours as for the NASDAQ.
    @property
    def name(self):
        return "xses"

    @property
    def tz(self):
        return "Asia/Singapore"

    @property
    def open_time(self):
        return pd.to_datetime("10:00:00", format="%H:%M:%S")

    @property
    def close_time(self):
        return pd.to_datetime("17:00:00", format="%H:%M:%S")

    @property
    def regular_holidays(self):
        # Source: https://www.sgx.com/ses-clearing-sustainability/clearing-suspensions-circuit-breakers-disclosure-records
        # Source: https://www.sgx.com/sites/default/files/holiday_cal_sgx.xls
        # The following regular holidays are observed by the SGX:
        return [
            "2021-01-01", # New Year's Day
            "2021-02-16", # Chinese New Year
            "2021-04-02", # Good Friday
            "2021-04-26", # Easter Monday
            "2021-05-03", # Labour Day
            "2021-05-19", # Vesak Day
            "2021-06-14", # Hari Raya Puasa
            "2021-08-09", # National Day
            "2021-09-24", # Mid-Autumn Festival
            "2021-10-12", # National Day (second part)
            "2021-11-05", # Deepavali
            "2021-12-22", # Christmas Eve
            "2021-12-23", # Christmas Day
            "2021-12-27", # Christmas Holiday
            "2021-12-30", # New Year's Eve
        ]

    @property
    def adhoc_holidays(self):
        # No ad hoc holidays specified.
        return []