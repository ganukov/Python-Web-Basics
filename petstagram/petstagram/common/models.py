from django.db import models
from petstagram.photos.models import Photo


class CommentText(models.Model):
    comment = models.TextField(max_length=300)
    # auto generated when comment is created !!!
    date_and_time = models.DateTimeField(auto_now_add=True)
    # the comment to relate to the photo! !!!
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)


class Like(models.Model):
    # the like to relate to the photo !!!
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
