from django.contrib import admin
from .models import Farm, ContactMessage

@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ('name', 'farm_type', 'overall_rating', 'difficulty', 'rates', "description", "tutorial_link")
    search_fields = ('name', 'farm_type')

admin.site.register(ContactMessage)