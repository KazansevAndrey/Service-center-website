from django.db import models

# Create your models here.
class Certificates(models.Model):
    file = models.FileField(upload_to='certificates')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертефикаты'

    def __str__(self):
        return f'{self.file}'