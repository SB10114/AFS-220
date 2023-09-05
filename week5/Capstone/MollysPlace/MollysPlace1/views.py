from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post



# def home(request):
#     return render(request, 'home.html', {})

# def page1(request):
#     return render(request, 'page1.html', {})

# def page2(request):
#     return render(request, 'page2.html', {})

# def page3(request):
#     return render(request, 'page3.html', {})

# def page4(request):
#     return render(request, 'page4.html', {})

class HomeView(ListView):
    model = Post 
    template_name = 'home.html'