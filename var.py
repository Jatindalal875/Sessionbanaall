
from decouple import config
from heroku3 import from_key
from os import getenv

class Var:
    API_ID = config("API_ID", "12834603")
    API_HASH = config("API_HASH", "84a5daf7ac334a70b3fbd180616a76c6")
    PYRO_SESSION = config("PYRO_SESSION", "BQACl6_2mdS2RyYkDYKlGnTgvFJf92hXksr_CghDIEhJJD1a9iZ0VkUvWDrRr8Z9acKj34tSYAYEbNqwTMkWzK6OzJ0MhkO4wrRnPIZNxxaLh37tk42JPt0ySMLw74kLfFHd_9xgugAltvsbTPvppshEz31qWJncaRpXSnqrMRFqwToMBY2pLP8ufOA2gOpQKIBG2B4kCj6HFLNj-JlbmRmUMTB3Sz0xs2kD0vW54lhJunSKgllZ2snbDZV8fzPqXIG-0MMwfvXh7IzhtsbwnUiVa-TI5ni9we55v3FmpNh60oQ5HeNOdtxIxD4jUdEx2nkVJ-uG08A8IgpS35Bl6xc6AAAAAWnSKskA")
