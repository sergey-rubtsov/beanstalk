from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.mail import send_mail
from forms import ContactForm
from django.views.generic.edit import CreateView

class ContactView(CreateView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = None

    def get(self, request):
        contact_form = ContactForm()
        return render_to_response(self.template_name, locals(), context_instance = RequestContext( request ))

    def post(self, request):
        if request.method == 'POST':
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                new_contact = contact_form.save()
                # send_mail(
                #     'Feedback Submitted',
                #     'Thanks for submitting your suggestion.',
                #     settings.DEFAULT_FROM_EMAIL,
                #     [new_contact.contact_email],
                # )
                return render_to_response('contact_added.html',
                              {'contact': new_contact},
                              RequestContext(request))
            else:
                error_fields = contact_form.errors.keys()
                for each_field in error_fields:
                    contact_form.fields[each_field].widget.attrs['class'] = 'textbox_error'
        else:
            contact_form = ContactForm()
        return render_to_response(self.template_name, locals(), context_instance = RequestContext( request ))