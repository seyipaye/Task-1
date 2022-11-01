from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def say_hello(request): 
    qs =  { "slackUsername": "seyipaye", "backend": True, "age": 22, "bio": "I am a senior python dev" }
    #data = serialize("json", qs, fields=('title', 'content'))
    return JsonResponse(qs)
