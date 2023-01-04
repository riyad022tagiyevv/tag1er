import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    
    
    BOT_ID = int(os.environ.get("BOT_ID", "5631477617"))
    OWNER_ID = int(os.environ.get("OWNER_ID", "5663585448"))
    
