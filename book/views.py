from django.shortcuts import render

from book.models import Book, Author, Comments, User, Adreess


def boook(request):
    if request.method == 'POST':
        search = request.POST['search']
        all_books = Book.objects.filter(title__icontains=search) | Book.objects.filter(author__icontains=search)
        if boook:
            return render(request, 'Book.html', {'books': all_books, "value": search, "message": "Succisfully"})
        else:
            return render(request, 'Book.html', {'books': all_books, "value": search, "message": "Not found"})
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


def address(request):
    if request.method == 'POST':
        search = request.POST['search']
        all_address = Adreess.objects.filter(address__icontains=search)
        if Adreess:
            return render(request, 'Adress.html', {"address": all_address, "value": search, "message": "Succisfully"})
        else:
            return render(request, 'Adress.html', {"address": all_address, "value": search, "message": "Not fount"})

    address = Adreess.objects.all()
    return render(request, 'Adress.html', {"address": address})