from django import forms
from .models import BlogComment, Contact, Blog

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        # fields = "__all__"
        fields = ("first_name", "last_name", "e_mail","phone_number","contact_message")
        # exclude = ("first_name",)

        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            "e_mail": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            "phone_number": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            "contact_message": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message'})
        }