from django.shortcuts import render

from django.contrib import admin
from django.urls import path, include


def home(request):
    return render(request, 'conversation')


def login(request):
    return render(request, 'core')


def main(request):
    return render(request, 'dashboard')


def item(request):
    return render(request, 'item')
