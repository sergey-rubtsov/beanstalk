__author__ = 'Serg'

from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('contact.views',
    url( r'^$', ContactView.as_view(), name='contact'),
)
