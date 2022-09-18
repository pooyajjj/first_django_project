from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import date
from .models import Article
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from blog.serializers import BlogModelSerializer
# Create your views here.



class GetAllDate(APIView):
    def get(self, request):
        query = Article.objects.all()
        serializers = BlogModelSerializer(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


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
        'article': get_object_or_404(Article, slug = slug, status = 'p')
}
    return render(request, 'blog/detail.html', context)

def index(request):
    return render(request, 'blog/index.html')


def about(request):
    return render(request, 'blog/about.html')

def post(request):
    return render(request, 'blog/example_post.html')

def contact(request):
    return render(request, 'blog/contact.html')