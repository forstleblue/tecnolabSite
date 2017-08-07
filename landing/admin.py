from django.contrib import admin
from landing.models import *
from image_cropping import ImageCroppingMixin
from django.forms import CheckboxSelectMultiple


class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


class SliderAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_img", "titolo", "active")


class LoghiAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_img", "titolo")


class PageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("titolo", "pub_date", "active")
    formfield_overrides = {
		models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }



admin.site.register(Slider, SliderAdmin)
admin.site.register(Loghi, LoghiAdmin)
admin.site.register(Page, PageAdmin)
