from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello dude')

def new(request):
    return HttpResponse('Hello New')