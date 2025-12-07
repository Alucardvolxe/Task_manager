import django_filters
from .models import Tasks
class Taskfilter(django_filters.FilterSet):
    date_added = django_filters.DateFilter(field_name='date_added__date')
    reminder_time = django_filters.DateFilter(field_name='reminder_time__date')
    class Meta:
        model = Tasks
        fields = {
            'title':['exact'],
            'number_repeat':['exact'],
            'date_added':['exact','lt','gt'],
            'reminder_time':['exact','lt','gt']
        }
    