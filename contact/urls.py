__author__ = 'Serg'

from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('contact.views',
    url( r'^$', form, name='form'),
    url( r'^submit/', submit, name='submit'),
)
