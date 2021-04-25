from django.db import models

# Create your models here.
class Display(models.Model):
    title =  models.CharField(max_length=50)
    image = models.ImageField(upload_to='home/')

    class Meta:
        verbose_name = 'Display'
        verbose_name_plural = 'Displays'

    def __str__(self):
        return self.title
    