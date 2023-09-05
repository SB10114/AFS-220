from django.urls import path
from .views import HomeView, ArticleDetailView, ArticleDetailView2, ArticleDetailView3, ArticleDetailView4, AddPostView


urlpatterns = [
     path('', HomeView.as_view(), name = "home"),
     path('article/<int:pk>', ArticleDetailView.as_view(), name= 'articleDetail'),
     path('article1/<int:pk>', ArticleDetailView2.as_view(), name= 'articleDetail2'),
     path('article2/<int:pk>', ArticleDetailView3.as_view(), name= 'articleDetail3'),
     path('article3/<int:pk>', ArticleDetailView4.as_view(), name= 'articleDetail4'),
     path('add_post/', AddPostView.as_view(), name= 'add_post')
]
