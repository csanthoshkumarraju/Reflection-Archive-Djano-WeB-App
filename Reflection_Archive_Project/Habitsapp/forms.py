from django import forms
from .models import HabitModel

class HabitForm(forms.ModelForm):
    class Meta:
        model = HabitModel
        fields = ['habit']
        widgets = {
            'habit': forms.TextInput(attrs={'placeholder': 'Add a habit', 'class': 'habit-add-input', 'required': 'required'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['habit'].label = ''
