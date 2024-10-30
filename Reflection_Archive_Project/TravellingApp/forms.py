from django import forms
from .models import TravelModel

class TravelForm(forms.ModelForm):
    class Meta:
        model = TravelModel
        fields = ['destination']  
        widgets = {
            'destination': forms.TextInput(attrs={'placeholder': 'Add a travel destination', 'class': 'travel-add-input'})  # Updated placeholder and class
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['destination'].label = ''  
