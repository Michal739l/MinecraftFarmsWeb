from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Farm(models.Model):
    FARM_TYPE_CHOICES = [
        ('iron', 'Iron Farm'),
        ('gold', 'Gold Farm'),
        ('wood', 'Wood Farm'),
        ('food', 'Food Farm'),
        ('mob', 'Mob Farm'),
    ]

    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
        ('expert', 'Expert'),
    ]

    name = models.CharField(max_length=100)
    overall_rating = models.IntegerField(choices=[(i, f"{i} Stars") for i in range(1, 6)], default=1)
    farm_type = models.CharField(max_length=50, choices=FARM_TYPE_CHOICES, default='iron')
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES)
    rates = models.CharField(max_length=100)
    description = models.TextField()
    tutorial_link = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    username = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.username} at {self.created_at}"