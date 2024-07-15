from django.shortcuts import render
from .models import Dokon, Tarix, Profil


def accaunt(request):
    return render(request, 'accaunt/accaunt.html')


def dokon(request):
    dokon = Dokon.objects.all()
    return render(request, 'accaunt/dokon.html', {'dokon': dokon})


def tarix(request):
    tarix = Tarix.objects.all()
    return render(request, 'accaunt/tarix.html', {'tarix': tarix})


def profil(request):
    profil = Profil.objects.all()
    return render(request, 'accaunt/profil.html', {'profil': profil})