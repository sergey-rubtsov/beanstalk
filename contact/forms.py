__author__ = 'Serg'

from django import forms
from models import Contact

class ContactForm(forms.ModelForm):

    def __init__( self, *args, **kwargs ):
        super(forms.ModelForm, self ).__init__( *args, **kwargs )

        self.fields['telephone_number'].widget.attrs['class'] = ' rsform-block-tel'
        self.fields['telephone_number'].label = 'Telephone'

        self.fields['contact_name'].widget.attrs['class'] = ' rsform-block-name'
        self.fields['contact_name'].label = 'Name'

        self.fields['contact_email'].widget.attrs['class'] = ' rsform-block-email'
        self.fields['contact_email'].label = 'Email'

        self.fields['message'].widget.attrs['class'] = ' rsform-block-send'

    class Meta:
        model = Contact