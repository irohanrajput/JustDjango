from django.http import HttpResponse
from django.shortcuts import render


def landing_page(request):
    return HttpResponse("<h1>This is the landing page of this site</h1>")