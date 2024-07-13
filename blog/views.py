from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def kutibxona(request):
    return render(request, 'blogs/kutibxona.html')


@login_required()
def kitob(request):
    return render(request, 'blogs/kitob.html')


@login_required()
def users(request):
    return render(request, 'blogs/foyda.html')