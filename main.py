"""
Cloud-scheduler HTTP trigger for 50CentBot
"""
import os
from datetime import datetime
from typing import Dict, Optional, Text
from pathlib import Path
import random
from flask import Request
from local.memegenerator import make_meme
from local.currency import Currency
from local.twitter import Twitter
from decimal import Decimal

c = Currency()
t = Twitter()


def main(request: Request):
    """
    Responds to an HTTP request.

    Parameters:
    ----------
    request (flask.Request):
        HTTP request object.
    """

    exchange_rate: str = c.get_exchange_rate("USD", "BRL")

    dec = Decimal(exchange_rate)
    visible_rate: str = f"R${(dec/2).quantize(Decimal('1.00'))}".replace(".", ",")
    tweet_rate: str = f"R${dec.quantize(Decimal('1.00'))}".replace(".", ",")

    files = Path("./local/images").glob("*.*")

    random_filename = random.choice([f for f in files])

    make_meme(topString="", bottomString=visible_rate, filename=random_filename)
    t.post(tweet_rate)

    return True


if __name__ == "__main__":
    main("foo")
