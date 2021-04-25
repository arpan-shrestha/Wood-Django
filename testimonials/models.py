from django.db import models

# Create your models here.
class Testimonials(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='testimonials/')

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
    
    def __str__(self):
        return self.name
    