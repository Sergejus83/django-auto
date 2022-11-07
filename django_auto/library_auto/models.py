from django.db import models
import uuid
# Create your models here.

class AutoModel(models.Model):
    name_auto = models.CharField('Auto name', max_length=100, help_text="Enter name of car")
    model_auto = models.CharField('Auto model', max_length=100, help_text="Enter model of car")

    def __init__(self) -> str:
        return f"{self.name_auto} {self.model_auto}"

    class Meta:
        ordering = ['name_auto', 'model_auto']
    

class Auto(models.Model):
    plate_number = models.CharField('license plate number', max_length=50)
    model_auto = models.ForeignKey(AutoModel, verbose_name="auto model", on_delete=models.CASCADE)
    vin_code = models.CharField('VIN code', max_length=50)
    client = models.CharField('client', max_length=100)

    def __init__(self) -> str:
        return f"{self.plate_number} : {self.model_auto} : {self.vin_code} : {self.client}"