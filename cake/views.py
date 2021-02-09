# food/views.py
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index2.html', context=None)