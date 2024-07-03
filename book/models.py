from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    objects = None
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Book(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    discriptions = models.TextField()
    count = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.ManyToManyField(Author)
    # img = models.ImageField(upload_to='books/', default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Adress(models.Model):
    objects = None
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Comments(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ManyToManyField(Book)
    adres = models.ManyToManyField(Adress)

    def __str__(self):
        return self.text
