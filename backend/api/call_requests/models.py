from django.db import models
from django.utils.timezone import now
from accounts.models import User
from django.utils.timezone import now
# Create your models here.

class CallRequest(models.Model):
    '''Заявки на звонки'''
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.name}, {self.phone_number}'
    
    class Meta:
        verbose_name = 'Заявка на звонок'
        verbose_name_plural = 'Заявки на звонок'