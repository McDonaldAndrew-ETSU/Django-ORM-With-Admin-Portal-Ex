from django.db import models

# Create your models here.
class Racer(models.Model):
    name = models.CharField(max_length=200)
    skill = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Car(models.Model):
    car_name = models.CharField(max_length=200)
    car_power = models.IntegerField()
    year = models.DateTimeField()
    racer_name = models.ForeignKey('Racer', on_delete=models.PROTECT)
    def __str__(self):
        return self.car_name