from django.db import models
from grossesse.models import Grossesse

class Note(models.Model):
    titre = models.CharField(max_length=255)
    objet = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    grossesse_id = models.ForeignKey(Grossesse, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre
