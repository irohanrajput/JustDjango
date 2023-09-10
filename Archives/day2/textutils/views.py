# This file was created manually by me
from django.http import HttpResponse


#it takes an arguement "request"
def index(request):  
    return HttpResponse("day2")

def day2(request):  
    return HttpResponse("Learnt about django file structure,some basic commands,managing urls, views etc")

def newfunction(request):  
    return HttpResponse("this is how we manage and call the functions")
    