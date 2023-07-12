from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=50)


class Country(models.Model):
    name = models.CharField(max_length=100)
    languages = models.ManyToManyField(to=Language)
