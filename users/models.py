from django.db import models


class Dokon(models.Model):
    kitob = models.CharField(max_length=120)
    kitob_narxi = models.IntegerField()

    def __str__(self):
        return self.kitob


class History(models.Model):
    kitob = models.CharField(max_length=120)
    kitob_narxi = models.IntegerField()

    def __str__(self):
        return self.kitob
