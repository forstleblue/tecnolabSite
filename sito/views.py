from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.template.loader import render_to_string
from sito.models import *
from django.core.mail import send_mail
from filer.models import *




def HomePage(request):
    slider_list = Slider.objects.filter(active=True).order_by('id')
    fiere_list = Fiere.objects.filter(attiva_slider=True).order_by('id')
    stand_list = Stand.objects.filter(attiva_slider=True).order_by('id')
    showroom_list = Showroom.objects.filter(attiva_slider=True).order_by('id')
    context = {'slider_list':slider_list,
                'fiere_list':fiere_list,
                'stand_list':stand_list,
                'showroom_list':showroom_list}
    return render_to_response('index.html', context, context_instance=RequestContext(request))




def HomePageDue(request):
    slider_list = Slider.objects.filter(active=True).order_by('id')
    fiere_list = Fiere.objects.filter(attiva_slider=True).order_by('id')
    stand_list = Stand.objects.filter(attiva_slider=True).order_by('id')
    showroom_list = Showroom.objects.filter(attiva_slider=True).order_by('id')
    context = {'slider_list':slider_list,
                'fiere_list':fiere_list,
                'stand_list':stand_list,
                'showroom_list':showroom_list}
    return render_to_response('index2.html', context, context_instance=RequestContext(request))



def HomePageTre(request):
    slider_list = Slider.objects.filter(active=True).order_by('id')
    fiere_list = Fiere.objects.filter(attiva_slider=True).order_by('id')
    stand_list = Stand.objects.filter(attiva_slider=True).order_by('id')
    showroom_list = Showroom.objects.filter(attiva_slider=True).order_by('id')
    context = {'slider_list':slider_list,
                'fiere_list':fiere_list,
                'stand_list':stand_list,
                'showroom_list':showroom_list}
    return render_to_response('index3.html', context, context_instance=RequestContext(request))
    


def AziendaPage(request):
    filer_list = Image.objects.filter(folder_id = 1)
    context = {'filer_list':filer_list}
    return render_to_response('studio.html', context, context_instance=RequestContext(request))




def FierePage(request):
	categoria_list = Fiere.objects.filter(active=True).order_by('titolo')
	context = {'categoria_list':categoria_list}
	return render_to_response('fiere.html', context, context_instance=RequestContext(request))



def FiereProvincia(request, post_id):
    categoria_list = Fiere.objects.filter(provincia_id=post_id).order_by('titolo')
    context = {'categoria_list':categoria_list}
    return render_to_response('fiere-provincia.html', context, context_instance=RequestContext(request))



def StandPage(request, post_id):
	categoria_list = Stand.objects.filter(fiera_id = post_id).order_by('titolo')
	titolo = Fiere.objects.get(pk=post_id)
	context = {'categoria_list':categoria_list,
				'titolo':titolo}
	return render_to_response('stand.html', context, context_instance=RequestContext(request))



def StandProvincia(request, post_id):
    categoria_list = Stand.objects.filter(provincia_id = post_id).order_by('titolo')
    titolo = Province.objects.get(pk=post_id)
    context = {'categoria_list':categoria_list,
                'titolo':titolo}
    return render_to_response('stand-provincia.html', context, context_instance=RequestContext(request))



def ShowroomPage(request):
    showroom_list = Showroom.objects.all().order_by('titolo')
    context = {'showroom_list':showroom_list}
    return render_to_response('showroon.html', context, context_instance=RequestContext(request))


def ShowroomProvincia(request, post_id):
    showroom_list = Showroom.objects.filter(provincia_id=post_id).order_by('titolo')
    context = {'showroom_list':showroom_list}
    return render_to_response('showroon-provincia.html', context, context_instance=RequestContext(request))


def ShowroomDetails(request, post_id):
    showroom = Showroom.objects.get(pk=post_id)
    filer_list = Image.objects.filter(folder_id = showroom.album)
    context = {'showroom':showroom,
                'filer_list':filer_list}
    return render_to_response('showroom-detail.html', context, context_instance=RequestContext(request))



def CaseHistory(request):
    casehistory_list = Casehistory.objects.all().order_by('titolo')
    context = {'casehistory_list':casehistory_list}
    return render_to_response('casehistory.html', context, context_instance=RequestContext(request))


def CaseHistoryDetail(request, post_id):
    case = Casehistory.objects.get(pk=post_id)
    filer_list = Image.objects.filter(folder_id = case.album).order_by('name')
    context = {'case':case,
                'filer_list':filer_list}
    return render_to_response('case-detail.html', context, context_instance=RequestContext(request))



def GalleryView(request):
    gallery_list = Gallery.objects.filter(active=True).order_by('titolo')
    context = {'gallery_list':gallery_list}
    return render_to_response('gallery.html', context, context_instance=RequestContext(request))


def ContactView(request):
    showroom_list = Showroom.objects.all()
    context = {'showroom_list':showroom_list}
    return render_to_response('contatti.html', context, context_instance=RequestContext(request))


def StandDetail(request, post_id):
	stand = Stand.objects.get(pk = post_id)
	filer_list = Image.objects.filter(folder_id = stand.album)
	context = {'stand':stand,
				'filer_list':filer_list}
	return render_to_response('dettaglio.html', context, context_instance=RequestContext(request))


def ProvinceView(request):
    province_list = Province.objects.all().order_by('titolo')
    context = {'province_list':province_list}
    return render_to_response('province.html', context, context_instance=RequestContext(request))


### setting language session
def language(request, language='it'):
    response = HttpResponse("setting language to %s" % language)
    response.set_cookie('lang', language)
    request.session['lang'] = language
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))