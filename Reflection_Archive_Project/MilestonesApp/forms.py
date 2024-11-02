from django import forms
from .models import MilestoneModel

class MilestoneForm(forms.ModelForm):
    class Meta:
        model = MilestoneModel
        fields = ['milestone']
        widgets = {
            'milestone': forms.TextInput(attrs={
                'class': 'Milestones-add-input',
                'placeholder': 'Add a Milestone',
                'required': 'required',  
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['milestone'].label = ''
