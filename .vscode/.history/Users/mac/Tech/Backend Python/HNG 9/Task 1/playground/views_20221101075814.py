from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def say_hello(request): 
    qs = { 
    "title":"Super Cool Title",  
    "content":"Some really cool content" }
    #data = serialize("json", qs, fields=('title', 'content'))
    return JsonResponse({})
