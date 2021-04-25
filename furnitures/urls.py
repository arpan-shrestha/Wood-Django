from django.urls import path
from . import views

app_name = 'furnitures'


urlpatterns = [
    path('',views.furnitures, name='furnitures'), 
]