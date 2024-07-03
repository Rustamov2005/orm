from django.contrib.auth.models import User
from django.shortcuts import render

from book.models import Book, Author, Comments, User, Adress


def boook(request):
    book = Book.objects.all()
    context = {'book': book}
    return render(request, 'Book.html', context=context)


def author(request):
    author = Author.objects.all()
    context = {'author': author}
    return render(request, 'Author.html', context=context)


def comments(request):
    commint = Comments.objects.all()
    context = {'comments': commint}
    return render(request, 'comments.html', context=context)


def users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users.html', context=context)


def address(request):
    address = Adress.objects.all()
    context = {'Olma': address}
    return render(request, 'Adress.html', context=context)