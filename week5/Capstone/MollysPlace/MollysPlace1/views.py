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

# class Blog1View(CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'articleDetail.html'