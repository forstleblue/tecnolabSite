from __future__ import unicode_literals
from django.db import models
from image_cropping import ImageRatioField, ImageCropField
from datetime import datetime, timedelta, time, date
from django.utils.timesince import timesince
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from filer.fields.folder import FilerFolderField
from taggit.managers import TaggableManager
from tinymce.models import HTMLField
from django.utils import timezone
from django import forms

# Create your models here.
class Slider(models.Model):
    titolo = models.CharField(max_length=100, verbose_name="Titolo")
    #titolo_uk = models.CharField(max_length=100, verbose_name="Titolo UK")
    image = models.ImageField(blank=True, null=True, upload_to='slider_landing')
    #scritta = models.TextField(null=True, blank=True)
    #scritta_uk = models.TextField(null=True, blank=True)
    #didascalia = models.TextField(null=True, blank=True)
    #didascalia_uk = models.TextField(null=True, blank=True)
    #link = models.TextField(null=True, blank=True)
    revolution = ImageRatioField('image', '1170x500', verbose_name="1170x500")
    #slider = ImageRatioField('image', '1920x1280', verbose_name="1920x1280")
    pub_date = models.DateTimeField('date published')
    active = models.BooleanField('attiva',
                                    default=False)

    def image_img(self):
        if self.image:
            return u'<img src="%s" style="width:300px"/>' % self.image.url
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Slider Landing Page"
        ordering = ['titolo']



class Loghi(models.Model):
    titolo = models.CharField(max_length=100)
    #link = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='loghi')
    #thumb = ImageRatioField('image', '312x135', verbose_name="312x135")
    miniatura = ImageRatioField('image', '300x300', verbose_name="300x300")

    def image_img(self):
        if self.image:
            return u'<img src="%s" style="width:200px"/>' % self.image.url
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Loghi"
        ordering = ['titolo']



class Page(models.Model):
    titolo = models.CharField(max_length=100)
    #titolo_uk = models.CharField(max_length=250, null=True, blank=True)
    #sottotitolo = models.CharField(max_length=250, null=True, blank=True)
    #sottotitolo_uk = models.CharField(max_length=250, null=True, blank=True)
    #link = models.CharField(max_length=250, null=True, blank=True)
    #body = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    #body_uk = models.TextField(null=True, blank=True, verbose_name="Descrizione Inglese")
    #image = models.ImageField(blank=True, null=True, upload_to='landing')
    #cropping = ImageRatioField('image', '500x281', verbose_name="500x281")
    #slidepage = ImageRatioField('image', '870x480', verbose_name="870x480")
    #album = FilerFolderField(null=True, blank=True)
    slider = models.ManyToManyField(Slider, null=True, blank=True, verbose_name="Seleziona Immagini Slider")
    loghi = models.ManyToManyField(Loghi, null=True, blank=True, verbose_name="Seleziona Loghi")
    active= models.BooleanField('attiva', default=False)
    tags = TaggableManager(verbose_name="Parole chiave", blank=True)
    pub_date = models.DateTimeField('date published')

    def image_img(self):
        if self.image:
            return u'<img src="%s" style="width:300px"/>' % self.image.url
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Landing Page"
