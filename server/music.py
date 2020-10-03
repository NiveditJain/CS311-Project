class Music:

    def __init__(self):
        self.uploadCompleted = False
        self.votes = 0
        self.filename = None
        self.name = None

    def __str__(self):
        if self.name is None:
            return 'Upload Not Yet Done'
        return self.name
