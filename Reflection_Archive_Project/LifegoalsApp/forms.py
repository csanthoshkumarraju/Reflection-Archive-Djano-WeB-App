from django import forms
from .models import GoalModel

class GoalForm(forms.ModelForm):
    class Meta:
        model = GoalModel
        fields = ['goal']
        widgets = {
            'goal': forms.TextInput(attrs={'class': 'goal-add-input', 'placeholder': 'Add a goal', 'required': True}),
        }
