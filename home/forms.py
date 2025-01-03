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
                'style': 'width: 40%; padding: 10px; font-size: 16px;'
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter Name',
                'class': 'form-control',
                'style': 'width: 30%; padding: 10px; font-size: 16px;'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter Email',
                'class': 'form-control',
                'style': 'width: 50%; padding: 10px; font-size: 16px;'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Enter Message',
                'class': 'form-control',
                'style': 'width: 100%; padding: 10px; font-size: 16px; height: 250px;'
            }),
        }
