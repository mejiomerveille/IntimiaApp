from django.db import models
from grossesse.models import Grossesse


# Create your models here.

class Symptome(models.Model):
    nom = models.CharField(max_length=100)
    intensite = models.CharField(max_length=2)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    grossesse_id = models.ForeignKey(Grossesse, on_delete=models.CASCADE)
