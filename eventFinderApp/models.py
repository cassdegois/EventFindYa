from django.db import models


class Event(models.Model):
    event_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    start_time = models.DateTimeField('start time and date')
    end_time = models.DateTimeField('end time and date')
    host = models.CharField(max_length=200)
    categories = models.ManyToManyField('Category')
    attendees = models.ManyToManyField('Users')

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)
    events = models.ManyToManyField(Event)
    category_id = models.CharField(max_length=50)
    
class Users(models.Model):
    user_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    events = models.ManyToManyField(Event)