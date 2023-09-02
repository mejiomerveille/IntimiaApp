from django.db import models

class RendezVous(models.Model):
    nom_medecin = models.CharField(max_length=100)
    profession_medecin = models.CharField(max_length=100)
    telephone_medecin = models.CharField(max_length=20)
    date_rendezvous = models.DateField()
    heure_rendezvous = models.TimeField()
    poids_mere = models.FloatField()
    rappel_notification = models.BooleanField(default=False)
    notes = models.TextField(blank=True)


    from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    reminder = models.BooleanField()

    def __str__(self):
        return f"Appointment with {self.doctor.name} on {self.date} at {self.time}"

class Question(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    question = models.TextField()

    def __str__(self):
        return self.question