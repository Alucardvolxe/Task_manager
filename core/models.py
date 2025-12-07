from django.db import models
from accounts.models import User
from django.utils import timezone
# Create your models here.
class Tasks(models.Model):
    class Timechoices(models.TextChoices):
        ONCE = '1','Once'
        DAILY = 'D','Daily'
        WEEKLY = 'WK','Weekly'
        MONTHLY = 'M','Monthly'
        QUARTERLY = 'Q','Quarterly'
        BIANNUALLY = 'BI','BiannuaLly'
        YEARLY = 'YR','Yearly'

    title = models.CharField(max_length=250)
    date_added = models.DateTimeField(default =timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reminder_time = models.DateTimeField()
    number_repeat = models.CharField(max_length=200,choices=Timechoices.choices, default=Timechoices.ONCE)

    def __str__(self):
        return self.title