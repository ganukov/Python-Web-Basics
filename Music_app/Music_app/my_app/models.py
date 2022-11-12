from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
def name_validator(value):
    for char in value:
        if not char.is_digit() and not char.is_alpha and '_' not in value:
            raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')


class Profile(models.Model):
    username = models.CharField(max_length=15, validators=[MinLengthValidator(2), name_validator])
    email = models.EmailField()
    age = models.IntegerField(null=True, blank=True, validators=[MinLengthValidator(0)])


class Album(models.Model):
    album_name = models.CharField(max_length=30, unique=True)
    artist = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField()
    price = models.FloatField(validators=[MinLengthValidator(0)])
