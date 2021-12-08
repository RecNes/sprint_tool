from cal.models import Event
from django.forms import ModelForm, DateInput


class EventForm(ModelForm):
  class Meta:
    model = Event
    widgets = {
      'start_time': DateInput(attrs={'type': 'date'}, format='%m/%d/%Y'),
      'end_time': DateInput(attrs={'type': 'date'}, format='%m/%d/%Y'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    self.fields['start_time'].input_formats = '%m/%d/%Y'
    self.fields['end_time'].input_formats = '%m/%d/%Y'