from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return HttpResponse('test')

def create(request):
    return HttpResponse('create')