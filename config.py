# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "28528300")
    API_HASH = environ.get("API_HASH", "de0db40bc15ebea5b7ce123bf57a4eb9")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8147851203:AAFU9SeJGvC5HEA2L3ZoGk0oHJULwvR5oAY") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6506692502').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://envs.sh/JcL.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://Rahat:EGbbbvweNl6EFzf6@rahat.pizkp.mongodb.net/?retryWrites=true&w=majority&appName=Rahat")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Rahat")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002393575041'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "-1002215749047") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
