from django.db import models

# Create your models here.
class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='aboutus/')

    class Meta:
        verbose_name='about us'
        verbose_name_plural='about us'

    def __str__(self):
        return self.title

    