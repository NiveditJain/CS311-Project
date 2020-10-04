import settings
import os

TOTAL_OBJECTS = 0


class Music:

    votes = []

    def __init__(self, filename, name):
        global TOTAL_OBJECTS
        TOTAL_OBJECTS = TOTAL_OBJECTS + 1
        self.id = TOTAL_OBJECTS
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
        self.votes = self.votes + [vote]


class Vote:

    def __init__(self, typ):
        self.upvote = typ

    def value(self):
        if self.upvote:
            return settings.UPVOTE_VALUE
        else:
            return -settings.DOWNVOTE_VALUE


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

        return highest_voted

    def add_music(self, music):
        self.music_objs = self.music_objs + [music]

    def clean_music(self):
        os.remove(os.path.join(settings.STORAGE, self.playing.filename))
        self.playing = None


playlist = Playlist()
