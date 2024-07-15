from django.db import models


class Dokon(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to="kitob/")
    commints = models.CharField(max_length=300)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.Title


class Tarix(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to="kitob/")
    commints = models.CharField(max_length=300)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.Title


class Profil(models.Model):
    pass




