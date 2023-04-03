from django.urls import path
from . import views



urlpatterns = [
    path('category/<str:slug>/',views.categories_page),
    path('<int:pk>/',views.PostDetail.as_view()),
    path('',views.PostList.as_view()),
    #path('<int:pnum>/',views.single_post_page),
    #path('', views.index),
]