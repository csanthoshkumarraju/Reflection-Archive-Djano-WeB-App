from django.db import models
from RA_Register_App.models import RA_RegistrationModel

class ExperienceModel(models.Model):
    user = models.ForeignKey(RA_RegistrationModel, on_delete=models.CASCADE, null=True)
    experience = models.TextField(null=True)
    status = models.CharField(max_length=500, null=True, default='Experience')

    def __str__(self):
        return self.experience[:50] 

