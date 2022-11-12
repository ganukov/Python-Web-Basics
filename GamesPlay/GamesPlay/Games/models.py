from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

CHOISES = (("Action", "Action"),
           ("Adventure", "Adventure"),
           ("Puzzle", "Puzzle"),
           ("Strategy", "Strategy"),
           ("Sports", "Sports"),
           ("Board/Card Game", "Board/Card Game"),
           ("Other", "Other"),
           )


def validate_rating(value):
    if 0.1 > value > 5.0:
        raise ValidationError('The rating can be between 0.1 and 5.0')


class Profile(models.Model):
    email = models.EmailField(null=False, blank=False)
    age = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(12)])
    password = models.CharField(null=False, blank=False, max_length=30)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True)


class Game(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False, unique=True)
    category = models.CharField(max_length=15, null=False, blank=False, choices=CHOISES)
    rating = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0.1),MaxValueValidator(5.0),])
    max_level = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1),])
    image_url = models.URLField(null=False, blank=False)
    summary = models.TextField(null=False, blank=False)
