from rest_framework import serializers
from .models import Tasks



class TaskSerialzer(serializers.ModelSerializer):
    
    message = serializers.CharField(max_length=500, required = True, allow_blank = False)
    number_repeat = serializers.IntegerField()
    reminder_time = serializers.DateTimeField()
    is_done = serializers.BooleanField(read_only = True)
    class Meta:
        model = Tasks
        fields = ['id','message','date_added','reminder_time','interval_min','number_repeat','is_done']



    def validate_message(self, value):
        if not value.strip():  
            raise serializers.ValidationError("This field cannot be empty")
        return value
