from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    img = models.ImageField(upload_to="author/", null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Book(models.Model):
    title = models.CharField(max_length=100)
    # slug = models.SlugField(max_length=100, unique=True)
    discriptions = models.TextField()
    count = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.ManyToManyField(Author)
    img = models.ImageField(upload_to='books/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Adress(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.name


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='comments/', null=True)
    book = models.ManyToManyField(Book)
    adress = models.ManyToManyField(Adress)

    def __str__(self):
        return self.text

