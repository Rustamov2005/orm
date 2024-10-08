from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Author, Comments, User, Adress
from .forms import BookForm


# @login_required()
def boook(request):
    if request.method == 'POST':
        search = request.POST['search']
        book = Book.objects.filter(title__icontains=search)
        if book:
            return render(request, 'Book.html', {'books': book, "value": search, "message": "Successfully"})
        else:
            return render(request, 'Book.html', {'books': book, "value": search, "message": "Not found"})
    book = Book.objects.all()
    return render(request, 'Book.html', {"books": book})


def author(request):
    if request.method == 'POST':
        search = request.POST['search']
        all_authors = Author.objects.filter(first_name__icontains=search) | Author.objects.filter(last_name__icontains=search)
        if Author:
            return render(request, 'Author.html', {'authors': all_authors, "search": search, "value": search, "message": "Succisfully"})
        else:
            return render(request, 'Author.html', {'authors': all_authors, "search": search, "message": "Not found"})
    author = Author.objects.all()
    return render(request, 'Author.html', {"authors": author})


def comments(request):
    if request.method == 'POST':
        search = request.POST['search']
        all_commint = Comments.objects.filter(text__icontains=search)
        if comments:
            return render(request, "comments.html", {"comment": all_commint, "search": search, "value": search, "message": "Succisfully"})
        else:
            return render(request, "comments.html", {"comment": all_commint, "search": search, "value": search, "message": "Not fount"})
    commint = Comments.objects.all()
    return render(request, 'comments.html', {"comment": commint})


def users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users.html', context=context)


def adreslar(request):
    if request.method == 'POST':
        search = request.POST['search']
        all_address = Adress.objects.filter(name__icontains=search)  # Assuming you are searching by 'name' field
        if all_address.exists():  # Check if queryset is not empty
            return render(request, 'Adress.html', {"address": all_address, "value": search, "message": "Successfully found"})
        else:
            return render(request, 'Adress.html', {"address": all_address, "value": search, "message": "Not found"})

    all_address = Adress.objects.all()
    return render(request, 'Adress.html', {"address": all_address})


@login_required()
def book_detail(request, slug):
    book = Book.objects.get(Book, slug=slug)
    if book:
        return render(request, 'book_detail.html', {"books": book, "message": "Succisfully"})
    else:
        return render(request, 'book_detail.html', {"books": book, "message": "Not found"})


def adrs_detail(request, id):
    adress = Adress.objects.get(id=id)
    if adress:
        return render(request, 'adres_detail.html', {"adress": adress, "message": "Succisfully"})
    else:
        return render(request, 'adres_detail.html', {"adress": adress, "message": "Not found"})


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book')
        else:
            return render(request, 'create_book.html', {"form": form, 'message_error': "qayirdadir o'zgarish bor"})
    form = BookForm()
    return render(request, 'create_book.html', {"form": form})


def book_detail_viwe(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'course_detail.html', {"books": book})


def book_delete_viwe(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('book')
