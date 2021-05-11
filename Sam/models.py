from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='posts_pics')
    date_posted = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Animal(models.Model):
    animal_types = (
        ("Katė", "Katė"),
        ("Šuo", "Šuo"),
        ("Arklys", "Arklys")
    )
    title = models.CharField(max_length=100)
    animal_type = models.CharField(max_length=100, choices=animal_types)
    content = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='animal_pics')


    def __str__(self):
        return self.title