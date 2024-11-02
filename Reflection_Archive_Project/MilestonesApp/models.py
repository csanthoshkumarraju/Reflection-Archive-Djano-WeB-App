from django.db import models
from RA_Register_App.models import RA_RegistrationModel

class MilestoneModel(models.Model):
    user = models.ForeignKey(RA_RegistrationModel, on_delete=models.CASCADE, null=True)
    milestone = models.TextField(null=True)
    date_added = models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return self.milestone

