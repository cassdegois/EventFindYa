from django.forms import ModelForm, SplitDateTimeField, ValidationError
from .models import Event, Category
from django.contrib.admin import widgets


class EventForm(ModelForm):
    start_time = SplitDateTimeField(widget=widgets.AdminSplitDateTime())
    end_time = SplitDateTimeField(widget=widgets.AdminSplitDateTime())

    class Meta:
        model = Event
        exclude = ["host"]

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        if start_time > end_time:
            raise ValidationError('Start time and date must be before end time and date.')


# class AccountForm(ModelForm):
   
#     class Meta:
#         model = Account
#         fields = [
#             'first_name',
#             'surname',
#             'email'
#         ]