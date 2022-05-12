from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def index(request):
    # return HttpResponse('<h1>Login success full </h1>')
    return render(request, 'ticket.html')


def loginUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username Or Password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def new_ticket(request):
    return render(request, 'ticket.html')