from django.db import models
from users.models import CustomUser

class Ticket(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    train_number = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    journey_date = models.DateField()
    journey_time = models.TimeField()
    pnr = models.CharField(max_length=100)
    status = models.CharField(default='Waiting', max_length=100)

class Train(models.Model):
    train_number = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    # Add more fields as per your requirements
