from django import forms
from .models import acheivements_model

class AchievementsForm(forms.ModelForm):
    class Meta:
        model = acheivements_model
        fields = ['acheiement']
        widgets = {
            'acheiement': forms.TextInput(attrs={'placeholder': 'Add an achievement', 'class': 'achievement-add-input'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['acheiement'].label = ''
