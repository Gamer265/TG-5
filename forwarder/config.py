from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5031210742:AAFD4jQnJVD4IZT0eTB9nXgkGMYXDExvobo"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    
    FROM_CHATS = [-1001434590863,-1001255359546,-1001488819353,-1001558904376,-1001504619251]# List of chat id's to forward messages from.
    TO_CHATS = [-1001727358945]# List of chat id's to forward messages to.

    REMOVE_TAG = False
    WORKERS = 32
   
    
