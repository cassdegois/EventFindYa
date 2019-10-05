from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'location', 'venue', 'start_time', 'end_time', 'categories', 'host', 'attendees']
