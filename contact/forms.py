__author__ = 'Serg'

from django import forms
from models import Contact

class ContactForm(forms.ModelForm):

    def __init__( self, *args, **kwargs ):
        super(forms.ModelForm, self ).__init__( *args, **kwargs )

        #self.fields[Contact.telephone_number.__str__()].widget.attrs['class'] = 'textbox'
        self.fields['telephone_number'].widget.attrs['class'] = 'textbox'
        self.fields['telephone_number'].label = 'Contact No'

        self.fields['contact_name'].widget.attrs['class'] = 'textbox'
        self.fields['contact_name'].label = 'Name'

        self.fields['contact_email'].widget.attrs['class'] = 'textbox'
        self.fields['contact_email'].label = 'Email'

        self.fields['message'].widget.attrs['class'] = 'textbox'

    class Meta:
        model = Contact