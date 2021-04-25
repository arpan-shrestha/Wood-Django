from django.shortcuts import render
from .models import Testimonials
# Create your views here.
def testimonials(request):
    testimonials = Testimonials.objects.all()

    context={
        'testimonials':testimonials,
    }
    return render(request, 'testimonial/company.html', context)
    
