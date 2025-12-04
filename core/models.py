from django.db import models
from accounts.models import User
from django.utils import timezone
# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=250)
    date_added = models.DateTimeField(timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reminder_time = models.DateTimeField()
    number_repeat = models.SmallIntegerField()