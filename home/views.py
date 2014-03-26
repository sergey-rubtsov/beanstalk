from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import TemplateView
from forms import MessageForm, EnquiryForm
import json
from django.shortcuts import *
from django.template import RequestContext
from linki.forms import *
from django import forms
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.context_processors import csrf

class HomeView(TemplateView):
    template_name = "home.html"

def new_enquiry(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('home'))
    else:
        form = EnquiryForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('home.html', context_instance=RequestContext(request))

def advert(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)

        message = 'something wrong!'
        if(form.is_valid()):
            print(request.POST['title'])
            message = request.POST['title']

        return HttpResponse(json.dumps({'message': message}))

    return render_to_response('contact/advert.html',
            {'form':EnquiryForm()}, RequestContext(request))

