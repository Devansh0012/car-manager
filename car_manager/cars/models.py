from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=100)
    #add photo field for adding upto 10 car images to the car model 
    photo = models.ImageField(upload_to='cars_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.user.username} - {self.make} {self.model} {self.year}"
    
