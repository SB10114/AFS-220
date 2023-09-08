from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm


class HomeView(ListView):
    model = Post 
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'articleDetails.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class Blog1View(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'articleDetails2.html'

class Blog2View(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'articleDetails3.html'

class Blog3View(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'articleDetails4.html'

class Blog4View(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'allAboutMolly.html'