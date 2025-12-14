from rest_framework import generics, request,viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Tasks
from.serializer import TaskSerialzer
from .filters import Taskfilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from .models import User  
from  django_q.tasks import schedule
from django.utils import timezone
from datetime import timedelta
from django_q.models import Task as QTask


def schedule_reminder(task):
    if task.reminder_time<timezone.now():
        task.reminder_time = timezone.now()+timedelta(seconds=10)
        task.save()
    schedule(
         'core.tasks.send_task',
         task.id,
         name=f'reminder_{task.id}',
         schedule_type = 'I',
         next_run = task.reminder_time,
         minutes = task.interval_min,
         repeats = task.number_repeat,
         group=f'reminder_{task.id}',
     )

class TaskViews(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerialzer
    permission_classes = [IsAuthenticated]
    filterset_class = Taskfilter
    filter_backends = [DjangoFilterBackend]
    


    def perform_create(self, serializer):
        task=serializer.save(user=self.request.user)
        schedule_reminder(task)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(user = self.request.user)
        return qs
    
    
    @action(
            # permission_classes =[IsAuthenticated],
            detail=False,
              methods=['get'],
                url_path='user-tasks')
    def Usertasks(self, request, *args,**kwargs):
        tasks=self.get_queryset().filter(user = request.user)
        serializer = self.get_serializer(tasks, many = True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['GET'], url_path="results")
    def results(self, request, pk=None):
        from django_q.models import Task
        from datetime import datetime
        
        task = self.get_object()
    
    
        q_results = QTask.objects.filter(
            group=f'reminder_{task.id}'
        ).order_by('-started')
        
        formatted_results = [q.result for q in q_results if q.result is not None and q.success]
        
        return Response({"status": "success", "results": formatted_results})