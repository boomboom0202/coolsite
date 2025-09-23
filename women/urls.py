from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('cats/<int:catid>/', categories, name='categories'),
    path('about/', about, name='about'),
    re_path(r'^archive/(?P<year>\d{4})/$', archive, name='archive'),
]