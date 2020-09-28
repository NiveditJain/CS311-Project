from django.db import models
from django.core.exceptions import ValidationError


class Music(models.Model):
    file_name = models.CharField(max_length=255)
    file = models.FileField()

    def __str__(self):
        return self.file_name


class Vote(models.Model):
    vote_choices = (
        (False, 'Downvote'),
        (True, 'Upvote')
    )
    song = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='votes')
    vote = models.BooleanField(choices=vote_choices)
    created_at = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.pk:
            raise ValidationError("vote is immutable")
        super(Vote, self).save(force_insert=False, force_update=False, using=None,
                               update_fields=None)
