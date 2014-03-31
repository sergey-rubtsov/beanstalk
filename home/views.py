from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import TemplateView
import json
from django.shortcuts import *
from django.template import RequestContext
from django import forms
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.context_processors import csrf

class HomeView(TemplateView):
    template_name = "home.html"