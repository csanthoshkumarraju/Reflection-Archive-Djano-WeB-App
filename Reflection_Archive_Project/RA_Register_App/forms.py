from django import forms
from .models import RA_RegistrationModel

class RA_registrationForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'register-input'}),  # Add class here
        label="Confirm Password"
    )

    class Meta:
        model = RA_RegistrationModel
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password']  
    
        widgets = {
    'password': forms.PasswordInput(attrs={'class': 'register-input'}),
    'first_name': forms.TextInput(attrs={'class': 'register-input'}),
    'last_name': forms.TextInput(attrs={'class': 'register-input'}),
    'email': forms.EmailInput(attrs={'class': 'register-input'}),
}


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")  

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")  

