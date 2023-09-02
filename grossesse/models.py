from django.db import models
from django.contrib.auth.models import User 
import datetime

class Grossesse(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return f"Grossesse {self.start_date} - {self.end_date}"
    
    def calculer_date_accouchement(self):
        return self.start_date + datetime.timedelta(days=280)
    
    def get_start_date(self):
        return self.start_date

    def save(self, *args, **kwargs):
        if not self.end_date:
            self.end_date = self.calculer_date_accouchement()
        super().save(*args, **kwargs)