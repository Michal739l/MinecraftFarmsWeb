from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Farm, ContactMessage

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="Password", help_text="")
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'Your Username',
            'email': 'Email Address',
        }
        help_texts = {
            'username': '',
            'email': '',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")


class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['name', 'overall_rating', 'farm_type', 'difficulty', 'rates', 'description', 'tutorial_link']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['username', 'message']