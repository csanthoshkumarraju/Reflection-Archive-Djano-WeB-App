from django.db import models
from RA_Register_App.models import RA_RegistrationModel

class MemoryModel(models.Model):
    user = models.ForeignKey(RA_RegistrationModel, on_delete=models.CASCADE, null=True)
    memory = models.TextField(null=True)
    status = models.CharField(max_length=500, null=True, default='Memory')

    def __str__(self):
        return self.memory[:50]

