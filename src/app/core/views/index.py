
from django.shortcuts import render
from django.http import HttpRequest


def index(request: HttpRequest):
    context = {
        'title': 'Мой заголовок',
        'items': ['Один', 'Два', 'Три']
    }
    
    return render(request, 'index.html', context)
    