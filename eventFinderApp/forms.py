from django.forms import ModelForm
from .models import Event, Category 

class EventForm(ModelForm):
    class Meta:
        model = Event 
        fields = {
            'name',
            'location',
            'venue',
            'start_time',
            'end_time',
            'categories',
            'host',
        }