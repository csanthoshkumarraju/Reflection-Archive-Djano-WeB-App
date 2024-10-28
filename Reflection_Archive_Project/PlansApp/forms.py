from django import forms
from .models import plan_model

class Plan_Form(forms.ModelForm):
    class Meta:
        model = plan_model
        fields = ['plan']
        widgets = {
            'plan': forms.TextInput(attrs={'class': 'plan-add-input', 'placeholder': 'Add a plan', 'required': True}),
        }
