"""tecnolab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from sito import views
import landing.views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePage, name='home'),
    url(r'^grigio/$', views.HomePageDue, name='homedue'),
    url(r'^scuro/$', views.HomePageTre, name='hometre'),
    url(r'^chisiamo/$', views.AziendaPage, name='chisiamo'),

    url(r'^fiere/$', views.FierePage, name='fiere'),
    url(r'^fiere-provincia/(?P<post_id>\d+)/$', views.FiereProvincia, name='fiere-provincia'),

    url(r'^stand/(?P<post_id>\d+)/$', views.StandPage, name='stand'),
    url(r'^stand-provincia/(?P<post_id>\d+)/$', views.StandProvincia, name='stand-provincia'),
    url(r'^dettaglio/(?P<post_id>\d+)/$', views.StandDetail, name='dettaglio'),

    url(r'^showroom/$', views.ShowroomPage, name='showroom'),
    url(r'^showroom-provincia/(?P<post_id>\d+)/$', views.ShowroomProvincia, name='showroom-provincia'),
    url(r'^showroom/(?P<post_id>\d+)/$', views.ShowroomDetails, name='showroom-detail'),

    url(r'^casehistory/$', views.CaseHistory, name='case-history'),
    url(r'^casehistory/(?P<post_id>\d+)/$', views.CaseHistoryDetail, name='casehistory-detail'),

    url(r'^province/$', views.ProvinceView, name='province'),
    url(r'^gallery/$', views.GalleryView, name='gallery'),
    url(r'^contatti/$', views.ContactView, name='contatti'),
    url(r'^language/(?P<language>[a-z\-]+)/$', views.language),

    url(r'^landing/$', landing.views.landingIndex, name='landing-indice'),
    url(r'^landing/(?P<post_id>\d+)/$', landing.views.landingDetail, name='landing-detail'),

    #sitemaps and robots
    url(r'^sitemap\.xml$', TemplateView.as_view(template_name='sitemap.xml', content_type='text/xml')),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/xml')),
]

if settings.DEBUG:  
        urlpatterns += patterns('',  
                                #REMOVE IT in production phase  
                                (r'^media/(?P<path>.*)$', 'django.views.static.serve',  
                                {'document_root': settings.MEDIA_ROOT})
          )