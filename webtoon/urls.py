from django.urls import path
from . import views
from django.urls import  include

urlpatterns = [
    path('',views.home),
    path('similar/<int:selected_image_id>/',views.find_similar_images),

]