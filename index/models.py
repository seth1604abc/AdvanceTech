from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=50, null=False, primary_key=True)

    def __str__(self):
        return self.name

class Unit(models.Model):
    number = models.CharField(max_length=50, null=False)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return self.number
