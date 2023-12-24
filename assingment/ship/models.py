from django.db import models

# Create your models here.
class Ship(models.Model):
    """
    This model will store imo number and ship name
    """
    imo_number = models.CharField(max_length=7, primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):

        return self.name + '-' + self.imo_number


class ShipPosition(models.Model):
    """
    This model will store position of ships
    """
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
