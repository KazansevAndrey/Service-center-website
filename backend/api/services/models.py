from django.db import models

# Create your models here.
class ServiceCategory(models.Model):
    """Названия категорий"""
    class Meta:
        verbose_name_plural = "Services categories"
    category_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    def __str__(self):
        return f"{self.category_name}"
    class Meta:
        verbose_name = 'Категория услуг'
        verbose_name_plural = 'Категории услуг'
        

class Service(models.Model):
    """Общая табличка услуг"""

    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    price = models.PositiveIntegerField()
    warranty_period = models.PositiveIntegerField()
    is_popular = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.category} {self.name}"
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        
