from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    start_time = models.DateTimeField('start time and date')
    end_time = models.DateTimeField('end time and date')
    host = models.ForeignKey(User, related_name = 'hosting_events', on_delete = models.CASCADE)
    categories = models.ManyToManyField('Category', related_name = 'events')
    attendees = models.ManyToManyField(User, related_name = 'attending_events')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
