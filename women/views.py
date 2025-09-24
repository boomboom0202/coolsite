from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from .models import *

menu = [{'title': "О нас", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}]


def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        
    }
    return render(request, 'women/index.html', context = context)

def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu' : menu})

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация") 

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>404 - Страница не найдена</h1>")

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с номером {post_id}")