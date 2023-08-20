from django.shortcuts import render
from django.contrib import admin

from django.http import HttpResponse

def index(request):
    return render(request, 'index.html',)