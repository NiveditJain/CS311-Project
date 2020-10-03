import os
import settings

if not os.path.exists(settings.STORAGE):
    print('STORAGE folder not found, Creating!')
    os.makedirs(settings.STORAGE)
    print('STORAGE folder Created at ' + settings.STORAGE)
