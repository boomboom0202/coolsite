from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from .models import *

def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', context={'title': 'Главная страница', 'posts': posts, 'menu': ['О нас', 'Добавить статью', 'Обратная связь', 'Войти']})

def about(request):
    return render(request, 'women/about.html', context={'title': 'О нас', 'menu': ['О нас', 'Добавить статью', 'Обратная связь', 'Войти']})

def categories(request, catid):
    print(request.GET)
    return HttpResponse(f"<h1>Страница категории {catid}</h1>")

def archive(request, year):
    if int(year) > 2025:
        return redirect( index, permanent=True)
    return HttpResponse(f"<h1>Архив по годам: {year}</h1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>404 - Страница не найдена</h1>")