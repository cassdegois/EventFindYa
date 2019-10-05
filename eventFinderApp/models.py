from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()

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

# class Account(models.Model):
#     first_name = models.CharField(max_length=50)
#     surname = models.CharField(max_length=50)
#     email = models.EmailField()


