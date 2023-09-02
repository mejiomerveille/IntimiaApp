from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    weight = models.FloatField()
    notes = models.TextField()
