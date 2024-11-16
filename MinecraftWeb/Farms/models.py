from django.db import models
from django.contrib.auth.models import User

class Farm(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, null=True, blank=True)
    tutorial_link = models.URLField(max_length=200, null=True, blank=True)
    difficulty = models.IntegerField(choices=[(i, i) for i in range(1, 6)], null=True, blank=True)
    efficiency = models.IntegerField(choices=[(i, i) for i in range(1, 6)], null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='farm_images/', null=True, blank=True)  # Přidáno pole pro obrázek

    def __str__(self):
        return self.name
