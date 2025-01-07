from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['subject', 'name', 'email', 'message']
        widgets = {
            'subject': forms.TextInput(attrs={
                'placeholder': 'Enter Subject',
                'class': 'form-control',
                'style': 'width: 100%; max-width: 500px; padding: 10px; font-size: 16px;'
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter Name',
                'class': 'form-control',
                'style': 'width: 100%; max-width: 500px; padding: 10px; font-size: 16px;'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter Email',
                'class': 'form-control',
                'style': 'width: 100%; max-width: 500px;  padding: 10px; font-size: 16px;'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Enter Message',
                'class': 'form-control',
                'style': 'width: 100%; padding: 10px; font-size: 16px; height: 130px;'
            }),
        }
