import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    
    
    BOT_ID = int(os.environ.get("BOT_ID", "5631477617"))
    OWNER_ID = int(os.environ.get("OWNER_ID", "5663585448"))
    API_ID = int(os.environ.get("API_ID", "12210813"))
    API_HASH = os.environ.get("API_HASH",  "e42eeae11a2f96bcfc5ec3b46a30adad")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5631477617:AAFrf8wg07Anl5MpmZj3LMPCEZkJw966hCM")
