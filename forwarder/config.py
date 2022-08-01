from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5231885300:AAGvyhETmGvS0cJHbuXkVsKcMC2eu0bkySw"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    
    FROM_CHATS = [-1001217338584,-1001261550869,-1001372142453,-1001668681402,-1001787061183,-1001617036243]# List of chat id's to forward messages from.
    TO_CHATS = [-1005267822653]# List of chat id's to forward messages to.

    REMOVE_TAG = False
    WORKERS = 32
   
    
