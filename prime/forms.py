from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact_us
        fields = ['name', 'subject','email', 'message']