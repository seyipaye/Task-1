from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def say_hello(request): 
    qs = { 
    "title":"Super Cool Title",  
    "content":"Some really cool content" }
    data = serialize("json", qs, fields=('title', 'content'))
    return HttpResponse(data, content_type="application/json")
