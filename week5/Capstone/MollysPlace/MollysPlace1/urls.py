from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView


urlpatterns = [
     path('', HomeView.as_view(), name = "home"),
     path('article/<int:pk>', ArticleDetailView.as_view(), name= 'articleDetail'),
     path('add_post/', AddPostView.as_view(), name= 'add_post'),
     # path('articleDetails', Blog1View.as_view(), name = 'articleDetail' )
]
