__author__ = 'Serg'

from django import forms
from models import Contact

class ContactForm(forms.ModelForm):

    def __init__( self, *args, **kwargs ):
        super(forms.ModelForm, self ).__init__( *args, **kwargs )

        self.fields['telephone_number'].widget.attrs['class'] = ' required'
        self.fields['telephone_number'].widget.attrs['id'] = ' telephone'
        self.fields['telephone_number'].label = 'Telephone:'

        self.fields['contact_name'].widget.attrs['class'] = ' required'
        self.fields['contact_name'].widget.attrs['id'] = ' name'
        self.fields['contact_name'].label = 'Your name:'

        self.fields['contact_email'].widget.attrs['class'] = ' required'
        self.fields['contact_email'].widget.attrs['id'] = ' email'
        self.fields['contact_email'].label = 'Email:'

        self.fields['message'].widget.attrs['class'] = ' required'
        self.fields['message'].widget.attrs['id'] = ' message'
        self.fields['message'].label = 'Message:'

    class Meta:
        model = Contact