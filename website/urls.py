from django.urls import path, include
from website.views import index, sobre, login, servicos, dashboard, cadastro, contato

urlpatterns = [
    path('', index),
    path('sobre', sobre),
    path('login', login),
    path('cadastro', cadastro),
    path('contato', contato),
    path('servicos', servicos),
    path('dashboard', dashboard)
]
