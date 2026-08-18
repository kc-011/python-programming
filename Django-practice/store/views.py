from django.shortcuts import HttpResponse, render

def home(request):
    data = {
    'name':'Karan',
    'age':23,
    'skills':['Python', 'Django', 'HTML', 'SQL']
    }
    # return HttpResponse('Hello. My first Django page.')
    return render(request, 'index.html', context=data)


# Create your views here.
