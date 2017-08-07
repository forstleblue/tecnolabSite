from __future__ import unicode_literals

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



class Slider(models.Model):
    titolo = models.CharField(max_length=100, verbose_name="Titolo")
    image = models.ImageField(blank=True, null=True, upload_to='slider')
    scritta = models.TextField(null=True, blank=True)
    didascalia = models.TextField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    croppingslide = ImageRatioField('image', '1140x487', verbose_name="slider")
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
        verbose_name_plural = "Slider"
        ordering = ['id']



class Province(models.Model):
    titolo = models.CharField(max_length=100, verbose_name="Titolo")
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Province"
        ordering = ['titolo']




class Fiere(models.Model):
    titolo = models.CharField(max_length=100)
    titolo_uk = models.CharField(max_length=250, null=True, blank=True)
    sottotitolo = models.CharField(max_length=250, null=True, blank=True)
    sottotitolo_uk = models.CharField(max_length=250, null=True, blank=True)
    provincia = models.ForeignKey(Province, null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    body = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    body_uk = models.TextField(null=True, blank=True, verbose_name="Descrizione Inglese")
    image = models.ImageField('Logo Neutro', blank=True, null=True, upload_to='fiere')
    cropping = ImageRatioField('image', '500x281', verbose_name="500x281")
    #crop hover
    image_hover = models.ImageField('Logo Hover', blank=True, null=True, upload_to='fiere')
    cropping_hover = ImageRatioField('image_hover', '500x281', verbose_name="500x281 hover")
    album = FilerFolderField(null=True, blank=True)
    attiva_slider = models.BooleanField('attiva in slider', default=False)
    active= models.BooleanField('attiva', default=False)
    tags = TaggableManager(verbose_name="Parole chiave", blank=True)

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
        verbose_name_plural = "Fiere"
        ordering = ['titolo']




class Stand(models.Model):
    fiera = models.ForeignKey(Fiere, null=True, blank=True)
    titolo = models.CharField(max_length=100)
    titolo_uk = models.CharField(max_length=250, null=True, blank=True)
    sottotitolo = models.CharField(max_length=250, null=True, blank=True)
    sottotitolo_uk = models.CharField(max_length=250, null=True, blank=True)
    azienda = models.CharField(max_length=250, null=True, blank=True, verbose_name="Azienda")
    link = models.CharField(max_length=250, null=True, blank=True)
    provincia = models.ForeignKey(Province, null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True, verbose_name="Location")
    body = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    body_uk = models.TextField(null=True, blank=True, verbose_name="Descrizione Inglese")
    image = models.ImageField(blank=True, null=True, upload_to='stand')
    cropping = ImageRatioField('image', '500x281', verbose_name="500x281")
    slidepage = ImageRatioField('image', '870x480', verbose_name="870x480")
    croppingthumb = ImageRatioField('image', '595x335', verbose_name="595x335")
    croppingslide = ImageRatioField('image', '1140x487', verbose_name="1140x487")
    croppingcarousel = ImageRatioField('image', '198x132', verbose_name="198x132")
    croppingrender = ImageRatioField('image', '1199x674', verbose_name="1199x674")
    designthumb = ImageRatioField('image', '500x469', verbose_name="Design Miniatura")
    designbig = ImageRatioField('image', '1200x800', verbose_name="Design HD", free_crop=True)
    designnews = ImageRatioField('image', '1200x1125', verbose_name="News")
    planimetria = models.ImageField(blank=True, null=True, upload_to='planimetria')
    planimetria_crop = ImageRatioField('planimetria', '1200x800', verbose_name="Design HD", free_crop=True)
    attiva_slider= models.BooleanField('attiva in slider', default=False)
    album = FilerFolderField(null=True, blank=True)
    active= models.BooleanField('attiva', default=False)
    tags = TaggableManager(verbose_name="Parole chiave", blank=True)

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
        verbose_name_plural = "Stand"
        ordering = ['titolo']




class Showroom(models.Model):
    titolo = models.CharField(max_length=100)
    titolo_uk = models.CharField(max_length=250, null=True, blank=True)
    sottotitolo = models.CharField(max_length=250, null=True, blank=True)
    sottotitolo_uk = models.CharField(max_length=250, null=True, blank=True)
    azienda = models.CharField(max_length=250, null=True, blank=True, verbose_name="Azienda")
    link = models.CharField(max_length=250, null=True, blank=True)
    provincia = models.ForeignKey(Province, null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    body = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    body_uk = models.TextField(null=True, blank=True, verbose_name="Descrizione_uk")
    image = models.ImageField(blank=True, null=True, upload_to='showroom')
    cropping = ImageRatioField('image', '500x281', verbose_name="500x281")
    slidepage = ImageRatioField('image', '870x480', verbose_name="870x480")
    croppingthumb = ImageRatioField('image', '595x335', verbose_name="595x335")
    croppingslide = ImageRatioField('image', '1140x487', verbose_name="1140x487")
    croppingcarousel = ImageRatioField('image', '198x132', verbose_name="198x132")
    croppingrender = ImageRatioField('image', '1199x674', verbose_name="1199x674")
    designthumb = ImageRatioField('image', '500x469', verbose_name="Design Miniatura")
    designbig = ImageRatioField('image', '1200x800', verbose_name="Design HD", free_crop=True)
    designnews = ImageRatioField('image', '1200x1125', verbose_name="News")
    album = FilerFolderField(null=True, blank=True)
    planimetria = models.ImageField(blank=True, null=True, upload_to='planimetria')
    planimetria_crop = ImageRatioField('planimetria', '1200x800', verbose_name="Design HD", free_crop=True)
    attiva_slider = models.BooleanField('attiva in slider', default=False)
    active = models.BooleanField('attiva', default=False)
    tags = TaggableManager(verbose_name="Parole chiave", blank=True)

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
        verbose_name_plural = "Showroom"




class Casehistory(models.Model):
    titolo = models.CharField(max_length=100)
    titolo_uk = models.CharField(max_length=250, null=True, blank=True)
    sottotitolo = models.CharField(max_length=250, null=True, blank=True)
    sottotitolo_uk = models.CharField(max_length=250, null=True, blank=True)
    azienda = models.CharField(max_length=250, null=True, blank=True, verbose_name="Azienda")
    link = models.CharField(max_length=250, null=True, blank=True)
    provincia = models.ForeignKey(Province, null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    body = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    body_uk = models.TextField(null=True, blank=True, verbose_name="Descrizione Inglese")
    image = models.ImageField(blank=True, null=True, upload_to='casehistory')
    cropping = ImageRatioField('image', '500x281', verbose_name="500x281")
    slidepage = ImageRatioField('image', '870x480', verbose_name="870x480")
    croppingthumb = ImageRatioField('image', '595x335', verbose_name="595x335")
    croppingslide = ImageRatioField('image', '1140x487', verbose_name="1140x487")
    croppingcarousel = ImageRatioField('image', '198x132', verbose_name="198x132")
    croppingrender = ImageRatioField('image', '1199x674', verbose_name="1199x674")
    designthumb = ImageRatioField('image', '500x469', verbose_name="Design Miniatura")
    designbig = ImageRatioField('image', '1200x800', verbose_name="Design HD", free_crop=True)
    designnews = ImageRatioField('image', '1200x1125', verbose_name="News")
    album = FilerFolderField(null=True, blank=True)
    planimetria = models.ImageField(blank=True, null=True, upload_to='planimetria')
    planimetria_crop = ImageRatioField('planimetria', '1200x800', verbose_name="Design HD", free_crop=True)
    attiva_slider = models.BooleanField('attiva in slider', default=False)
    active = models.BooleanField('attiva', default=False)
    tags = TaggableManager(verbose_name="Parole chiave", blank=True)

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
        verbose_name_plural = "Case History"



class Gallery(models.Model):
    titolo = models.CharField(max_length=100)
    titolo_uk = models.CharField(max_length=250, null=True, blank=True)
    body = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    body_uk = models.TextField(null=True, blank=True, verbose_name="Descrizione Inglese")
    image = models.ImageField(blank=True, null=True, upload_to='gallery')
    cropping = ImageRatioField('image', '500x281', verbose_name="500x281")
    slidepage = ImageRatioField('image', '870x480', verbose_name="870x480")
    croppingthumb = ImageRatioField('image', '595x335', verbose_name="595x335")
    croppingslide = ImageRatioField('image', '1140x487', verbose_name="1140x487")
    active = models.BooleanField('attiva', default=False)

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
        verbose_name_plural = "Gallery"








