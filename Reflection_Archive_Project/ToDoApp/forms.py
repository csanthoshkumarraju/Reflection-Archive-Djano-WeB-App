from django import forms
from .models import todo_model

class Todo_Form(forms.ModelForm):
    class Meta:
        model = todo_model
        fields = ['todo']
        widgets = {
            'todo': forms.TextInput(attrs={'placeholder': 'Add a todo task', 'class': 'todo-add-input'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['todo'].label = ''
