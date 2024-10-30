from django.db import models
from RA_Register_App.models import RA_RegistrationModel
# Create your models here.

class acheivements_model(models.Model):
    user = models.ForeignKey(RA_RegistrationModel,on_delete=models.CASCADE,null=True)
    acheiement = models.TextField(null=True)
    achievment_status = models.CharField(max_length=500,default="achievement",null=True)

    def __str__(self) -> str:
        return self.acheiement