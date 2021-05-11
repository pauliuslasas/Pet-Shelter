from django.urls import path
from . import views
from .views import AnimalDetailView, PostDetailView


urlpatterns = [
    path('', views.home, name="sam-home"),
    path('about/', views.about, name="sam-about"),
    path('arkliai/', views.arkliai, name="sam-arkliai"),
    path('kates/', views.kates, name="sam-kates"),
    path('sunys/', views.sunys, name="sam-sunys"),
    path('parama/', views.parama, name="sam-parama"),
    path('kontaktai/', views.kontaktai, name="sam-kontaktai"),
    path('news/', views.news, name="sam-news"),
    path('globotiniai/', views.globotiniai, name="sam-globotiniai"),
    path('animal/<int:pk>/', AnimalDetailView.as_view(), name="animal-detail"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),


]
