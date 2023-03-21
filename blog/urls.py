from django.urls import path
from .views import (
    HomePageView, PostDetailView, GamingPostView, AnimePostView, ProgrammingPostView
    )
from . import views




urlpatterns = [
    path('', HomePageView.as_view(), name='Blog-Home-Page'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.AboutPage, name='About-Page'),
    path('anime/', AnimePostView.as_view(), name='anime-page'),
    path('programming/', ProgrammingPostView.as_view(), name='prog-page'),
    path('gaming/', GamingPostView.as_view(), name='gaming-page'),
    path('contact/', views.ContactPage, name='Contact-page'),
]