from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.template.loader import render_to_string
from landing.models import *
from django.core.mail import send_mail
from filer.models import *

# Create your views here.
def landingIndex(request):
	context = {'page_list': Page.objects.all().order_by('-id')}
	return render_to_response('app2/index.html', context, context_instance=RequestContext(request))



def landingDetail(request, post_id):
	page = Page.objects.get(pk = post_id)
	context = {'page':page}
	return render_to_response('app2/detail.html', context, context_instance=RequestContext(request))
