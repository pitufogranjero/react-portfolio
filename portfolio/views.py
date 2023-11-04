# from django.http import HttpResponse
from django.shortcuts import render

# def greeting(request):
#     return HttpResponse('hello')

# def goodbye(request):
#     return HttpResponse('goodbye')

# def adult(request,age):
#     if age >= 18:
#         return HttpResponse('over 18')
#     else:
#         return HttpResponse('under 18')
    
# def simple(request):
#     return render(request, 'simple.html', {})

# def dynamic(request, name):
#     categories = ['code','design','marketing']
#     context = {'name' : name, 'categories' : categories}
#     return render(request, 'dynamic.html', context)

# def statics(request):
#     return render(request, 'statics.html', {})

def index(request):
    return render(request, 'index.html', {})

# def herencia(request):
#     return render(request, 'herencia.html', {})

# def ejemplo(request):
#     return render(request, 'ejemplo.html', {})

# def otra(request):
#     return render(request, 'otra.html', {})

def portfolio(request):
    return render(request, 'portfolio.html', {})
