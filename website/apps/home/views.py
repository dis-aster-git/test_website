from django.shortcuts import render
from website.apps.news.models import Post
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'home/index.html', {})

def about(request):
    return render(request, 'home/about.html', {})

def contact(request):
    return render(request, 'home/contact.html', {})

def data(request):
    return render(request, 'home/data.html', {})

def support(request):
    return render(request, 'home/support.html', {})

def team(request):
    return render(request, 'home/team.html', {})

def tech(request):
    return render(request, 'home/tech.html', {})

def overview(request):
    return render(request, 'home/overview.html', {})

def error(request):
    return render(request, 'home/error.html', {})

def news(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'home/news.html',  {'posts': posts})

def home_jp(request):
    return render(request, 'home/index_jp.html', {})

def about_jp(request):
    return render(request, 'home/about_jp.html', {})
    
def team_jp(request):
    return render(request, 'home/team_jp.html', {})
    
def tech_jp(request):
    return render(request, 'home/tech_jp.html', {})

def overview_jp(request):
    return render(request, 'home/overview_jp.html', {})