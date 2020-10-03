import settings
import os

TOTAL_OBJECTS = 0


class Music:
    def __init__(self, filename, name):
        global TOTAL_OBJECTS
        TOTAL_OBJECTS = TOTAL_OBJECTS + 1
        self.id = TOTAL_OBJECTS
        self.votes = []
        self.filename = filename
        self.name = name

    def __str__(self):
        if self.name is None:
            return 'Upload Not Yet Done'
        return self.name

    def get_value(self):
        value = 0
        for vote in self.votes:
            value = value + vote.value()
        return value

    def add_vote(self, vote):
        if type(vote) is not Vote:
            raise Exception('you can pass only Vote Objects')
        self.votes.append(vote)


class Vote:

    def __int__(self, upvote=False, downvote=False):
        self.upvote = upvote
        self.downvote = downvote

    def is_valid(self):
        return self.upvote ^ self.downvote

    def value(self):
        if self.is_valid():
            if self.upvote:
                return settings.UVOTE_VALUE
            else:
                return settings.DOWNVOTE_VALUE
        return 0


class Playlist:

    music_objs = []
    playing = None

    def get_next(self):
        highest_voted = None

        for music in self.music_objs:
            if highest_voted is None:
                highest_voted = music
            else:
                if highest_voted.get_value() < music.get_value():
                    highest_voted = music

        if highest_voted is not None:
            self.music_objs.remove(highest_voted)
            self.playing = highest_voted
            return os.path.join(settings.STORAGE, highest_voted.filename)

    def add_music(self, music):
        if type(music) is not Music:
            raise Exception('PlayList only accept Music Elements')

        self.music_objs = self.music_objs + [music]

    def clean_music(self):
        os.remove(os.path.join(settings.STORAGE, self.playing.filename))
        self.playing = None


playlist = Playlist()
