__author__ = 'Serg'

from django import forms
from models import Enquiry

class EnquiryForm(forms.ModelForm):

    class Meta:
        model = Enquiry
        fields = ('created', 'name', 'email', 'telephone', 'message')
        help_texts = {
            'name': 'Some useful help text',
        }
        error_messages = {
            'name': {
                'max_length': "Too long"
            }
        }

class MessageForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    telephone = forms.CharField(max_length=200)
    message = forms.CharField(max_length=10000, widget=forms.Textarea)

class MessageModelForm(forms.ModelForm):
    class Meta:
        model = Enquiry