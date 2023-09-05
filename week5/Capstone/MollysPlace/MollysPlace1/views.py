from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

class HomeView(ListView):
    model = Post 
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'articleDetails.html'

class ArticleDetailView2(DetailView):
    model = Post
    template_name = 'articleDetails2.html'

class ArticleDetailView3(DetailView):
    model = Post
    template_name = 'articleDetails3.html'

class ArticleDetailView4(DetailView):
    model = Post
    template_name = 'articleDetails4.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'