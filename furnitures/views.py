from django.shortcuts import render
from .models import Furnitures
# Create your views here.

def furnitures(request):
    furnitures = Furnitures.objects.all()

    context = {
        'furnitures' : furnitures,
    }
    return render(request, 'Furniture/furniture.html', context)

