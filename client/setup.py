import os
import settings

if not os.path.exists(settings.STORAGE):
    os.makedirs(settings.STORAGE)
