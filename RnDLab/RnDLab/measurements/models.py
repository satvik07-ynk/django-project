from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Equipment_Detail(models.Model):
    name = models.CharField('Equipment Name', max_length=120)
    weblink = models.URLField('Website Address', blank=True)
    datasheet = models.URLField('Datasheet Address', blank=True)
    scpilink = models.URLField('SCPI Web Link', blank=True)
    current_working_status = models.BooleanField()

    def __str__(self):
        return self.name

class Equipment_Connection(models.Model):
    name = models.ForeignKey(Equipment_Detail, blank=False, null=False, on_delete=models.CASCADE)
    scpi_address = models.CharField('Equipment Address',max_length=300)
    status = models.BooleanField()

    def __str__(self):
        return self.name.name

class Equipment_Type(models.Model):
    EquipmentType = models.TextChoices('EquipmentType', 'source measurement both')
    name = models.OneToOneField(Equipment_Detail, blank=False, null=False, on_delete=models.CASCADE)
    equipment_type = models.CharField(blank=False, choices=EquipmentType.choices, max_length=20)
    def __str__(self):
        return self.name.name

class Equipment_Parameter(models.Model):
    #name = models.OneToOneField(Equipment_Detail, blank=False, null=False, on_delete=models.CASCADE)
    name = models.ForeignKey(Equipment_Detail, blank=False, null=False, on_delete=models.CASCADE)
    parameter = models.CharField(max_length=100, blank=True)

    def __str__(self):
       return self.name.name