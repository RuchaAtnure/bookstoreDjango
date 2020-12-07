
from django.db import models

# Create your models her

class Book(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')




