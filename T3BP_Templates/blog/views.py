from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# def home(request):
#     return HttpResponse("<h1>blog page</h1>")

# this was printed directly, now we'll print by rendering the  html template "home.html" for homepage and "about.html" for about page.

# def about(request):
#     return HttpResponse("<h1>About Page</h1>")

def home(request):
    return render(request,'blog/home.html')
    # this will redirect to home.html file after searching for templates folder automatically
    # it goes like app->templates->appname->templates.html

def about(request):
    return HttpResponse("<h1>about blog page</h1>")
    #this will just print "about page"

def abouttemp(request):
    return render(request, 'blog/about.html')
