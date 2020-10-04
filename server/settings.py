from pathlib import Path
import os

# Port
PORT = 8080

# message exchange size
EXCHANGE_SIZE = 1024

# file storage folder
STORAGE = os.path.join(Path(__file__).resolve().parent, 'music')

# Upvote Value
UPVOTE_VALUE = 1

# DOWNVOTE_VALUE
DOWNVOTE_VALUE = 1
