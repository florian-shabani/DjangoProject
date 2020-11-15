from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Posts
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


class PostListView(ListView):
    model = Posts
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4


class UserPostListView(ListView):
    model = Posts
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Posts.objects.filter(author=user).order_by('-date_posted')


def about(request):
    return render(request, 'blog/about.html', {'title': "About"})


class PostDetailView(DetailView):
    model = Posts


class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Posts

    fields = ['title', 'content']

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
