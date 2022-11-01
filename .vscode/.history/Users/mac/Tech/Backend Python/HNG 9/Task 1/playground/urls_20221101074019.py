from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('playground/hello', views.say_hello)
]