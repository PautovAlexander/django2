from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<img src="https://cdn-images.dzcdn.net/images/cover/976ecd747edb60d200ebfb2b6433cd2f/500x500-000000-80-0-0.jpg" alt="Пример картинки">')

def about(request):
    return HttpResponse('<h1> about ME </h1>')
def mycourse(request):
    return HttpResponse('<h1> Its a cours of page </h1>')
