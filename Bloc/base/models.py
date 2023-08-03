from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class EventCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    lat = models.FloatField(default=0)
    long = models.FloatField(default=0)
    start_time = models.TimeField()
    end_time = models.TimeField()
    event_category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='event_pictures/')
    start_date = models.DateField()
    end_date = models.DateField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the event creator (User model)
    score = models.IntegerField(default=0)  # Event score or rating
    link = models.URLField(max_length=200, blank=True, null=True)
    distance = models.PositiveIntegerField(
        default=10, help_text='Maximum distance (in kilometers) you are willing to travel for events.'
    )