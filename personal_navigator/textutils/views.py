from django.http import HttpResponse

def index (request):
    return HttpResponse (
        f'<h1>Welcome to the HomePage  </br> </br>'
        f'<h1>click on the links below to go to pages  </br> </br>'
        f'<a href = "/removepunc">removepunc</a>  </br> </br>'
        f'<a href = "/capfirst">capfirst</a>  </br> </br>'
        f'<a href = "/newlineremove">newlineremove</a>  </br> </br>'
        f'<a href = "/spaceremove">spaceremove</a>  </br> </br>'
        f'<a href = "/charcount">charcount</a>  </br> </br>'
    )

from django.http import HttpResponse

def removepunc(request):
    return HttpResponse(
        f'remove punc </br>'
        f'<a href = "/">back to home</a>'
        )

def capfirst(request):
    return HttpResponse(
        f'remove punc </br>'
        f'<a href = "/">back to home</a>'
        )

def newlineremove(request):
    return HttpResponse(
        f'remove punc </br>'
        f'<a href = "/">back to home</a>'
        )

def spaceremove(request):
    return HttpResponse(
        f'remove punc </br>'
        f'<a href = "/">back to home</a>'
        )

def charcount(request):
    return HttpResponse(
        f'remove punc </br>'
        f'<a href = "/">back to home</a>'
        )



