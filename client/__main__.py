import runchecks
import client_functions
import argparse


parser = argparse.ArgumentParser(
    allow_abbrev=False,
    description='client interface for muZik!',
    epilog='Enjoy the Paaaarrrty !!!!')


parser.add_argument('-op', '--operation',
                    required=True,
                    choices=('upload', 'list', 'playing',
                             'downvote', 'upvote'),
                    action='store',
                    help='selects the operation to perform')

parser.add_argument('-id', type=int, required=False,
                    help='to select the id to vote for')

parser.add_argument('-l', '--listen', required=False,
                    action='store_true',
                    help='plays the song before voting')

parser.add_argument('-n', '--name', required=False,
                    help='name of song to upload')

parser.add_argument('-p', '--path', required=False,
                    help='path of music file to upload')

args = parser.parse_args()
print(args)

if args.operation == 'list':
    data = client_functions.get_playlist()

    if len(data) != 0:
        print('Name - id - votes')
        for element in data:
            print(f'{element[0]} - {element[1]} - {element[2]}')

    else:
        print('No Music in Playlist')


elif args.operation == 'playing':
    data = client_functions.get_playing()

    if data is not None:
        print(f'Now playing {data}')

    else:
        print('No song playing currently')


elif args.operation == 'upvote':
    if id is None:
        print('You must select the music id, select -id to set id')

    else:
        if args.listen:
            client_functions.listen(id)

        confirmation = input('confirm upvote [Y/N]?')

        if confirmation == 'Y' or confirmation == 'y':
            client_functions.upvote(id)


elif args.opertation == 'downvote':
    if id is None:
        print('You must select the music id, select -id to set id')

    else:
        if args.listen:
            client_functions.listen(id)

        confirmation = input('confirm downvote [Y/N]?')

        if confirmation == 'Y' or confirmation == 'y':
            client_functions.downvote(id)


elif args.operation == 'upload':
    if args.name is None:
        print('--name or -n not supplied')

    elif args.path is None:
        print('--path or -p not supplied')

    else:
        client_functions.playlist_add(args.name, args.filename)
