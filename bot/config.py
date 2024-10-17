import os
from os import getenv

class Config:
    TELEGRAM_TOKEN = getenv("TELEGRAM_TOKEN", None)
    PYRO_SESSION = getenv("PYRO_SESSION", "BQACl6_2mdS2RyYkDYKlGnTgvFJf92hXksr_CghDIEhJJD1a9iZ0VkUvWDrRr8Z9acKj34tSYAYEbNqwTMkWzK6OzJ0MhkO4wrRnPIZNxxaLh37tk42JPt0ySMLw74kLfFHd_9xgugAltvsbTPvppshEz31qWJncaRpXSnqrMRFqwToMBY2pLP8ufOA2gOpQKIBG2B4kCj6HFLNj-JlbmRmUMTB3Sz0xs2kD0vW54lhJunSKgllZ2snbDZV8fzPqXIG-0MMwfvXh7IzhtsbwnUiVa-TI5ni9we55v3FmpNh60oQ5HeNOdtxIxD4jUdEx2nkVJ-uG08A8IgpS35Bl6xc6AAAAAWnSKskA")
    TELEGRAM_APP_HASH= getenv('TELEGRAM_APP_HASH', "84a5daf7ac334a70b3fbd180616a76c6")
    TELEGRAM_APP_ID=int(getenv('TELEGRAM_APP_ID', "12834603"))
        
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
    if not TELEGRAM_TOKEN or not PYRO_SESSION:
        raise ValueError("PYRO_SESSION / TELEGRAM_TOKEN not set")
