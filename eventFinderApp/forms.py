from django.forms import ModelForm
from .models import Event, Category 

class EventForm(ModelForm):
    class Meta:
        model = Event 
        exclude = ['host']