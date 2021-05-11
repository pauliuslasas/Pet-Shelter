from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Post, Animal

# Create your views here.


class AnimalDetailView(DetailView):
    model = Animal

class PostDetailView(DetailView):
    model = Post


def home(request):
    context = {
        'posts': Post.objects.all().order_by('-id')[:3]
    }
    return render(request, 'Sam/index.html', context)


def about(request):
    return render(request, 'Sam/about.html')

def arkliai(request):
    return render(request, 'Sam/arkliai.html')

def kates(request):
    context = {
        'animals': Animal.objects.filter(animal_type="Katė").order_by('-id')
    }
    return render(request, 'Sam/kates.html', context)

def sunys(request):
    context = {
        'animals': Animal.objects.filter(animal_type="Šuo").order_by('-id')
    }
    return render(request, 'Sam/sunys.html', context)

def kontaktai(request):
    return render(request, 'Sam/kontaktai.html')

def parama(request):
    return render(request, 'Sam/parama.html')

def news(request):
    context = {
        'posts': Post.objects.all().order_by('-id')
    }
    return render(request, 'Sam/news.html', context)

def globotiniai(request):
    context = {
        'animals': Animal.objects.all().order_by('-id')
    }
    return render(request, 'Sam/globotiniai.html', context)