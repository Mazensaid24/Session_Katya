import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 29380940))

    API_HASH = os.environ.get("API_HASH", "a0d123fa03f3bf5e3942301ef74c04ab")
