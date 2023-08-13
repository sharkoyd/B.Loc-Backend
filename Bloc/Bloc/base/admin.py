from django.contrib import admin
from .models import EventCategory


@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    pass  # Since you don't need any additional customization
# Register your models here.

# Register your models here.
