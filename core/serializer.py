from rest_framework import serializers
from .models import Tasks



class TaskSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Tasks
        fields = ['title','reminder_time','number_repeat']