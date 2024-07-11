from django.db import models


class Kutibxona(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    books_types = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Kitob(models.Model):
    name = models.CharField(max_length=100)
    # kutibxona = models.ForeignKey(Kutibxona)

    def __str__(self):
        return self.name


class Users(models.Model):
    first_name = models.CharField(100)
    last_name = models.CharField(200)
    phonr_number = models.IntegerField

    def __str__(self):
        return self.first_name

