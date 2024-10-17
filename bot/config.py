import os
from os import getenv

class Config:
    TELEGRAM_TOKEN = getenv("TELEGRAM_TOKEN", "6233213793:AAHh5Nkoi8MNaodGInmONsQONCeatV6zZtc")
    PYRO_SESSION = getenv("PYRO_SESSION", "BQDD1ysAebGZ5Hs7Pf5_qswkDkqXxUzmlYIJCImZf9u7MsBnwDf4wDEcAGSp0jqimaueVORDwdKqeGavIqsAFRpWybFDcguk9MYczawm7A7MnksSUPS7bI1WsEsdpiSoUh3jchJ8-wnF7OIEKUMPR7R7I7xDTo459quF3TJSiNYUeGCxZMBN8dCNUF_40VQMsZQ0-24Zil0OpRvYjyBJ6w-6_OWFs2bu1Cl2MXD87_QoXgLc4WBtiBIIXALZYL_qf8x839dOlbPhmhibvo-Z41wJxwLhCfbCRnt164aRPcdHkObp5xOoUny6x_UN4M12ekAHmZutazRtgPmIjahVrmcVUzDl_AAAAAFp0irJAA")
    TELEGRAM_APP_HASH= getenv('TELEGRAM_APP_HASH', "84a5daf7ac334a70b3fbd180616a76c6")
    TELEGRAM_APP_ID=int(getenv('TELEGRAM_APP_ID', "12834603"))
        
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
    if not TELEGRAM_TOKEN or not PYRO_SESSION:
        raise ValueError("PYRO_SESSION / TELEGRAM_TOKEN not set")
