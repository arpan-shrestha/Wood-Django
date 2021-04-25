from django.shortcuts import render
from furnitures.models import Furnitures
from aboutus.models import AboutUs
from contact.forms import contactForm
from .models import Display
from testimonials.models import Testimonials
# Create your views here.
def home(request):
    furnitures = Furnitures.objects.all()
    about = AboutUs.objects.last()
    display = Display.objects.last()
    testimonials = Testimonials.objects.all()
    form = contactForm(request.POST)


    context = {
        'furnitures':furnitures,
        'about':about,
        'display':display,
        'testimonials':testimonials,
        'form':form,

    }
    
    return render(request,'home/index.html', context)

    