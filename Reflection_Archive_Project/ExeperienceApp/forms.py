from django import forms
from .models import ExperienceModel

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = ExperienceModel
        fields = ['experience'] 
        widgets = {
            'experience': forms.TextInput(attrs={
                'placeholder': 'Add an experience',
                'class': 'experience-add-input',
                'required': 'required'  
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['experience'].label = ''
