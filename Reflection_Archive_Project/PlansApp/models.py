from django.db import models
from RA_Register_App.models import RA_RegistrationModel

class plan_model(models.Model):
    user = models.ForeignKey(RA_RegistrationModel, on_delete=models.CASCADE,null=True)
    plan = models.CharField(max_length=255,null=True)
    status = models.CharField(max_length=50, default='Plan',null=True)

    def __str__(self):
        return self.plan

