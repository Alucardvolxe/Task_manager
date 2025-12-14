import django_filters
from .models import Tasks
class Taskfilter(django_filters.FilterSet):
    date_added = django_filters.DateFilter(field_name='date_added__date')
    reminder_time = django_filters.DateFilter(field_name='reminder_time__date')
    class Meta:
        model = Tasks
        fields = {
            'message':['exact'],
            'number_repeat':['exact'],

            'reminder_time':['exact','lt','gt']
        }
    