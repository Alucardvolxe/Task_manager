from django.db import models
from accounts.models import User
from django.utils import timezone
# Create your models here.
class Tasks(models.Model):

    message = models.CharField(max_length=500)
    date_added = models.DateTimeField(default =timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reminder_time = models.DateTimeField()
    interval_min = models.IntegerField(default=1)
    number_repeat = models.IntegerField()
    is_done = models.BooleanField(default=False)
    def __str__(self):
        return self.message