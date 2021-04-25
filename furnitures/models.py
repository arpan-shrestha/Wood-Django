from django.db import models

# Create your models here.
class Furnitures(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='furnitures/')

    class Meta:
        verbose_name = 'Furniture'
        verbose_name_plural = 'Furnitures'

    def __str__(self):
        return self.name
