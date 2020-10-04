import os
from pathlib import Path

# SERVE DETAILS
HOST = '192.168.29.229'
PORT = 8080

# maximum size per file allowed (in Bytes)
# 10 MB = 10*1024*1024 Bytes
MAX_FILE_SIZE = 10485760

# message exchange size
EXCHANGE_SIZE = 1024

# allowed extensions for music files
ALLOWED_EXTENSIONS = ['.mp3', '.wav', ]

# file storage folder
STORAGE = os.path.join(Path(__file__).resolve().parent, 'music')
