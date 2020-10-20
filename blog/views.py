from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts


# Create your views here.
# posts = [{
#     'author': 'CoreyMS',
#     'title': 'Blog Post 1',
#     'content': 'First post content',
#     'date_posted': 'August 07, 2018'
# },
#     {
#     'author': 'Florian',
#     'title': 'Blog Post 2',
#     'content': 'Second post content',
#     'date_posted': 'Novenmber 07, 2018'

# }]


def home(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': "About"})
