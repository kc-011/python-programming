from django.shortcuts import HttpResponse, render, redirect
from .models import Product
from .forms import ContactForm, RegisterForm
from django.contrib.auth import login

def home(request):
    # data = {
    # 'name':'Karan',
    # 'age':23,
    # 'skills':['Python', 'Django', 'HTML', 'SQL']
    # }
    # return HttpResponse('Hello. My first Django page.')
    # return render(request, 'index.html', context=data)
    products = Product.objects.all()
    print(request.user)
    print(request.user.is_authenticated)
    return render(request, 'index.html', context={'products':products})

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = ContactForm()

    return render(request, 'contact.html', context={'form':form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form':form})

