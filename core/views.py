from rest_framework import generics, request,viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Tasks
from.serializer import TaskSerialzer
from .filters import Taskfilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from .models import User   
class TaskViews(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerialzer
    permission_classes = [AllowAny]
    filterset_class = Taskfilter
    filter_backends = [DjangoFilterBackend]
    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(
            permission_classes =[IsAuthenticated],
            detail=False,
              methods=['get'],
                url_path='user-tasks')
    def Usertasks(self, request, *args,**kwargs):
        tasks=self.get_queryset().filter(user = request.user)
        serializer = self.get_serializer(tasks, many = True)
        return Response(serializer.data)

