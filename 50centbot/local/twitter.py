"""
Interactions with Twitter API
"""
import os
import time
from base64 import b64encode

from twython import Twython, TwythonError


class Twitter:
    def __init__(self):
        self.twitter: Twython = Twython(
            os.getenv("TWITTER_API_KEY"),
            os.getenv("TWITTER_API_SECRET_KEY"),
            os.getenv("TWITTER_ACCESS_TOKEN"),
            os.getenv("TWITTER_ACCESS_TOKEN_SECRET"),
        )

    def __upload_image(self) -> str:
        """
        Uploads image to Twitter. Returns its media id
        """
        with open("/tmp/50c.jpeg", "rb") as f:
            img = b64encode(f.read())
            i = 0
            while i < 10:
                try:
                    upload: dict = self.twitter.upload_media(
                        media=img, media_type="image/jpeg"
                    )
                    media_id: str = upload.get("media_id_string", "")
                except TwythonError as e:
                    print(str(e))
                    time.sleep(2)
                    continue
                else:
                    return media_id
            else:
                raise ValueError("Couldn't upload media.")

    def post(self, exchange_rate: str):
        status = f"Dólar valendo: {exchange_rate}"
        image_id = self.__upload_image()
        r = self.twitter.update_status(status=status, media_ids=[image_id])
