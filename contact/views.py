from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.mail import send_mail
from django.conf import settings
from forms import ContactForm
from home.views import HomeView

class ContactView(HomeView):
    template_name = "contact.html"
    form_class = ContactForm