from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render
from .models import Event
from .forms import EventForm


class IndexView(generic.ListView):
    template_name = 'eventFinderApp/index.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.all()


class EventView(generic.DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'


# class AddEventCreateView(generic.CreateView):
#     # using the create view we can just give it the variables 
#     # as the functionaity is already built in!
#     form_class = EventForm
#     template_name = 'eventFinderApp/addevent.html'
#     success_url = reverse_lazy('eventFinderApp:index')

def add_event(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/thanks/')
            form.save()
            return HttpResponseRedirect(reverse('eventFinderApp:index'))
        return render(request, 'eventFinderApp/add-event.html', {'eventform': form})
    # if a GET (or any other method) we'll create a blank form
    else:
        eventform = EventForm()
        return render(request, 'eventFinderApp/add-event.html', {'eventform': eventform})

def accounts(request):
    return render(request, 'eventFinderApp/account.html')
