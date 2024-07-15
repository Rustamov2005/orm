from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages


def login_vewes(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('books')  # books URL nomi to'g'ri ekanligiga ishonch hosil qiling
        else:
            for msg in login_form.error_messages:
                messages.error(request, f"{msg}: {login_form.error_messages[msg]}")
            return render(request, 'auth/login.html', {'form': login_form})
    else:
        login_form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': login_form})

def regeter_vewes(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        password2 = request.POST['password2']
        if password != password2:
            return render(request, 'auth/register.html', context={"message_password": "Error password!"})
        else:
            if User.objects.filter(username=username).exists():
                return render(request, 'auth/register.html', context={"message": "User alredy exists!"})
            new_user = User(first_name=first_name, last_name=last_name, email=email, username=username)
            new_user.set_password(password)
            new_user.save()
            return redirect('auth/login')
    return render(request, 'auth/register.html')


def logout_vewes(request):
    logout(request)
    return redirect('book/book')


