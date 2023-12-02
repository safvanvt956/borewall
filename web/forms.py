from django import forms
from django.utils.translation import gettext_lazy as _
from . models import Contact
from django.forms import widgets

class ContactForm(forms.ModelForm):
  
    class Meta:
        model = Contact
        exclude = ("timestamp",)
        widgets = {
            "fullname": widgets.TextInput(attrs={"class": "text-input", "placeholder": "First Name"}),
            "lastname": widgets.TextInput(attrs={"class": "text-input", "placeholder": "Last Name"}),
            "email": widgets.EmailInput(attrs={"class": "text-input", "placeholder": "Email "}),
            "phone": widgets.TextInput(attrs={"class": "text-input", "placeholder": "Phone"}),
            "message": widgets.TextInput(attrs={"class": "text-input", "placeholder": "Enquiry Description"}),     
        }