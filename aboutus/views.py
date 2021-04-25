from django.shortcuts import render
from .models import AboutUs
# Create your views here.
def aboutus(request):
    about = AboutUs.objects.last()

    context={
        'about': about,
    }
    return render(request, 'aboutus/aboutus.html', context)