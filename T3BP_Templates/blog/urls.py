from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="blog-home"), #this is for "something.com/blog" as this file contains all the urls of "blog" APP onlyz

    path('about/', views.about, name="blog-about"), #this is for "something.com/blog/about" 

    path('abouttemp/', views.abouttemp, name="blog-abouttemp"),

]