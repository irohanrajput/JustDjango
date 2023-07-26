from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# def home(request):
#     return HttpResponse("<h1>blog page</h1>")

# this was printed directly, now we'll print by rendering the  html template "home.html" for homepage and "about.html" for about page.

# def about(request):
#     return HttpResponse("<h1>About Page</h1>")

posts = [ 
    {
        'author':'CoreyMS',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted' : 'July 24, 2023'
    },
    {
        'author': 'Rohan',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 25, 2023'
    }
]

#we can pass this 'posts' in our template
# https://youtu.be/qDwdMDQ8oX4?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&t=1079



# this will redirect to home.html file after searching for templates folder automatically
    # it goes like app->templates->appname->templates.html
def home(request):
    context = {
        'posts': posts, 
    }
    return render(request,'blog/home.html', context)

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)
