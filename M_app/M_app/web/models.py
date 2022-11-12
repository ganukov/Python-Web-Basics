from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

GENRES_CHOICES = (
    ("Pop Music", "Pop Music"),
    ("Jazz Music", "Jazz Music"),
    ("R&B Music", "R&B Music"),
    ("Rock Music", "Rock Music"),
    ("Country Music", "Country Music"),
    ("Dance Music", "Dance Music"),
    ("Hip Hop Music", "Hip Hop Music"),
    ("Other", "Other"),
)


def validate_name(value):
    for char in value:
        if not char.isalpha() and not char.isdigit() and char != '_':
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore")


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        blank=False, null=False, max_length=15, validators=[MinLengthValidator(2), validate_name]
    )
    email = models.EmailField(blank=False, null=False)
    age = models.IntegerField(blank=True, null=True)


class Album(models.Model):
    name = models.CharField(
        unique=True, max_length=30, blank=False, null=False
    )
    artist = models.CharField(max_length=30, null=False, blank=False)
    genre = models.CharField(max_length=30, null=False, blank=False, choices=GENRES_CHOICES)
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0)])
    owned = models.ManyToManyField(
        Profile,
    )