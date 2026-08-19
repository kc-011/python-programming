from django.shortcuts import HttpResponse, render
from .models import Product
from .forms import ContactForm

def home(request):
    # data = {
    # 'name':'Karan',
    # 'age':23,
    # 'skills':['Python', 'Django', 'HTML', 'SQL']
    # }
    # return HttpResponse('Hello. My first Django page.')
    # return render(request, 'index.html', context=data)
    products = Product.objects.all()

    return render(request, 'index.html', context={'products':products})

def contact(request):
    form = ContactForm()

    return render(request, 'contact.html', context={'form':form})

