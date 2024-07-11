from django.shortcuts import render
from .models import Kutibxona, Kitob, Users
from django.contrib.auth.decorators import login_required


@login_required()
def kutibxona(request):
    kutibxona = Kutibxona.objects.all()
    return render(request, 'kutibxona.html', {"kutibxona": kutibxona})


@login_required()
def kitob(request):
    kitob = Kitob.objects.all()
    return render(request, 'kitob.html', {"kitob": kitob})


@login_required()
def users(request):
    usersa = Users.objects.all()
    return render(request, 'foyda.html', {"usersa": usersa})