from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def say_hello(request): 
    qs =  { "slackUsername": "seyipaye", "backend": Boolean, "age": Integer, "bio": String }
    #data = serialize("json", qs, fields=('title', 'content'))
    return JsonResponse(qs)
