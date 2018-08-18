from dataIO import fileIO
import os

false_strings = ["false", "False", "f", "F", "0", ""]

if fileIO("config.json", "check"):
    config = fileIO("config.json", "load")
else:
    config = {
        "consumer_key": os.environ["CONSUMER_KEY"],
        "consumer_secret": os.environ["CONSUMER_SECRET"],
        "access_token": os.environ["ACCESS_TOKEN"],
        "access_token_secret": os.environ["ACCESS_TOKEN_SECRET"]
    }