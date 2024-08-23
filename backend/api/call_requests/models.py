from django.db import models
from accounts.models import User
# Create your models here.

class CallRequest(models.Model):
    '''Заявки на звонки'''
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True)
    def __str__(self):
        return f'{self.name}, {self.phone_number}'
    
    class Meta:
        verbose_name = 'Заявка на звонок'
        verbose_name_plural = 'Заявки на звонок'