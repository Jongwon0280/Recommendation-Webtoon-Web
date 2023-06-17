from django.urls import path
from . import views
from django.urls import  include


urlpatterns = [
    #path('/webtoon/',include("webtoon.urls")),
    path('',views.main),
]