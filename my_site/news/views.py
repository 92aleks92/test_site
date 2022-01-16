from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def index(request):
    news = News.objects.order_by('-created_at')#сортировка новостей начиная с последней добавленной
    context = {'news': news,
               'title': 'Список нвовстей'
               }
    return render(request, template_name='news/index.html', context=context)


