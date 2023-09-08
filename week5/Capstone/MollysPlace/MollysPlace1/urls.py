from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, Blog1View, Blog2View, Blog3View, Blog4View


urlpatterns = [
     path('', HomeView.as_view(), name = "home"),
     path('article/<int:pk>', ArticleDetailView.as_view(), name= 'articleDetail'),
     path('add_post/', AddPostView.as_view(), name= 'add_post'),
     path('articleDetails2/', Blog1View.as_view(), name = 'articleDetails2' ),
     path('articleDetails3/', Blog2View.as_view(), name = 'articleDetails3' ),
     path('articleDetails4/', Blog3View.as_view(), name = 'articleDetails4' ),
     path('allAboutMolly/', Blog4View.as_view(), name = 'allAboutMolly' ),
]

