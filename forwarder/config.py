from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5534055979:AAGXBbAmX3AsM8OCXCeXdIJ52YGVMBJqaIg"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    
    FROM_CHATS = [-1001498726424,-1001579149062]# List of chat id's to forward messages from.
    TO_CHATS = [-1001711014960]# List of chat id's to forward messages to.

    REMOVE_TAG = False
    WORKERS = 16
   
    
