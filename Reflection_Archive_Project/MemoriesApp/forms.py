from django import forms
from .models import MemoryModel

class MemoryForm(forms.ModelForm):
    class Meta:
        model = MemoryModel
        fields = ['memory']
        widgets = {
            'memory': forms.TextInput(attrs={
                'placeholder': 'Add a memory',
                'class': 'memory-add-input',
                'required': 'required'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['memory'].label = ''
