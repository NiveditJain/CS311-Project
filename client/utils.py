import settings
import os


def verify_file(filename):

    extension = os.path.splitext(os.path.basename(filename))[1]

    if extension not in settings.ALLOWED_EXTENSIONS:
        print(f'got file extension {extension} which is not allowed')
        print('ALLOWED_EXTENSIONS are ' + str(settings.ALLOWED_EXTENSIONS))
        return False

    if not os.path.isfile(filename):
        print(f'{filename} not found or not a valid file!')
        return False

    file_size = os.path.getsize(filename)
    if file_size > settings.MAX_FILE_SIZE:
        print(f'Maximum allowed file size is {settings.MAX_FILE_SIZE} but got {file_size}')
        return False

    return True


def padded_message(message, length=settings.EXCHANGE_SIZE, padding_char = b' '):
    return message + padding_char*(length - len(message))