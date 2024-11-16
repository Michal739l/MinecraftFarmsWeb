from django.contrib import admin
from .models import Farm

@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'location', 'difficulty', 'efficiency')
    fields = ('name', 'owner', 'location', 'type', 'tutorial_link', 'difficulty', 'efficiency', 'description', 'image')
