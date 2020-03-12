"""
Gets data from the Alpha Vantage API
"""
from alpha_vantage.foreignexchange import ForeignExchange
from decimal import Decimal
import os


class Currency:
    def __init__(self):
        self.av = ForeignExchange(key=os.getenv("ALPHA_VANTAGE_KEY"))

    def get_exchange_rate(self, currency_from: str, currency_to: str) -> str:
        """
        Pulls the spot exchange rate for a given currency pair.
        """
        data: dict = self.av.get_currency_exchange_rate(
            from_currency=currency_from, to_currency=currency_to
        )[0]
        exchange_rate: str = data["5. Exchange Rate"]

        return exchange_rate
