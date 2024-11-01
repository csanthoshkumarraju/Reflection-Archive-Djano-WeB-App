from django.db import models
from RA_Register_App.models import RA_RegistrationModel

class GoalModel(models.Model):  
    user = models.ForeignKey(RA_RegistrationModel, on_delete=models.CASCADE, null=True)
    goal = models.CharField(max_length=255, null=True)  # Changed field name to goal
    status = models.CharField(max_length=50, default='Goal', null=True)  # Updated default status

    def __str__(self):
        return self.goal  