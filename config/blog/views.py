from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import Article

# Create your views here.

def home(request):
    context = {
        'articles': Article.objects.filter(status = 'p').order_by('-publish')
    }
    return render(request, 'blog/home.html', context)

def time(request):
    today = date.today()
    return HttpResponse(today)


def detail(request, slug):
    context = {
        'article': Article.objects.get(slug = slug)
}
    return render(request, 'blog/detail.html', context)

def index(request):
    return render(request, 'blog/index.html')


def about(request):
    return render(request, 'blog/about.html')