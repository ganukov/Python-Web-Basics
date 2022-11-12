from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator, MaxValueValidator
from django.db import models

CHOICES = (("Sports Car", "Sports Car"),
           ("Pickup", "Pickup"),
           ("Crossover", "Crossover"),
           ("Minibus", "Minibus"),
           ("Other", "Other"),)


class Profile(models.Model):
    username = models.CharField(max_length=10,
                                validators=[MinLengthValidator(2, message='The username must be a minimum of 2 chars')])
    email = models.EmailField(null=False, blank=False)
    age = models.IntegerField(null=False, blank=False,
                              validators=[MinValueValidator(18)])
    password = models.CharField(null=False, blank=False, max_length=30)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True)


class Car(models.Model):
    type = models.CharField(max_length=10, null=False, blank=False, choices=CHOICES)
    model = models.CharField(max_length=20, validators=[MinLengthValidator(2), ])
    year = models.IntegerField(null=False, blank=False,
                               validators=[MinValueValidator(1980, message='Year must be between 1980 and 2049'),
                                           MaxValueValidator(2049, message='Year must be between 1980 and 2049')])
    image_url = models.URLField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False, validators=[MinValueValidator(1), ])
