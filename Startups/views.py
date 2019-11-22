from django.http import HttpResponse
from django.shortcuts import render
import random


def index(request):
    context = {'test': [i for i in range(random.randrange(5, 10))]}
    return render(request, 'index.html', context=context)


def contact(request):
    return HttpResponse('You are at the contact page.')
