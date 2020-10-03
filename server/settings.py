from pathlib import Path
import os

# Port
PORT = 8080

# server will allow only these file extensions
ALLOWED_EXTENSIONS = ['.mp3', '.wav', ]

# maximum size per file allowed (in Bytes)
# 10 MB = 10*1024*1024 Bytes
MAX_FILE_SIZE = 10485760

# chunk size (in Bytes)
CHUNK_SIZE = 4096

# message exchange size
EXCHANGE_SIZE = 1024

# file storage folder
STORAGE = os.path.join(Path(__file__).resolve().parent, 'music')

# Upvote Downvote Value
UPVOTE_VALUE = 1

# DOWNVOTE_VALUE
DOWNVOTE_VALUE = 1
