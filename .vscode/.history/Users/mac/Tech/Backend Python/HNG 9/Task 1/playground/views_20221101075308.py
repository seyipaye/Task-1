from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def say_hello(request): 
    data = serialize("json", qs, fields=('title', 'content'))
    return HttpResponse(data, content_type="application/json")
