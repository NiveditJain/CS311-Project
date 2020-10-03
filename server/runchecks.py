# checking all settings
import settings
import warnings

print('Running SETTING Checks!')

if type(settings.PORT) is not int:
    raise Exception('settings.PORT must be an integer')

if settings.PORT < 0:
    raise Exception('settings.PORT Value cannot be negative')

if settings.PORT < 1024:
    warnings.warn('You are using a "Well Known Port"')

if settings.PORT > 65535:
    raise Exception('Invalid PORT number')

if len(settings.ALLOWED_EXTENSIONS) == 0:
    raise Exception('No extensions allowed')

for extension in settings.ALLOWED_EXTENSIONS:
    if type(extension) is not str:
        raise Exception('Only String extensions allowed')

if type(settings.MAX_FILE_SIZE) is not int:
    raise Exception('settings.MAX_FILE_SIZE should be an integer')

if settings.MAX_FILE_SIZE < 0:
    raise Exception('settings.MAX_FILE_SIZE should be greater than 0')

if settings.MAX_FILE_SIZE < 1048576:
    warnings.warn('settings.MAX_FILE_SIZE must be too less for files!')

if type(settings.EXCHANGE_SIZE) is not int:
    raise Exception('settings.EXCHANGE_SIZE must be an integer')

if settings.EXCHANGE_SIZE < 0:
    raise Exception('settings.EXCHANGE_SIZE must be positive')

if type(settings.STORAGE) is not str:
    raise Exception('settings.STORAGE must be a string')

if type(settings.UPVOTE_VALUE) is not int and type(settings.DOWNVOTE_VALUE) is not int:
    raise Exception('settings.UPVOTE_VALUE and settings.DOWNVOTE_VALUE must be integer')

print('All SETTINGS Checked!')