from django.contrib import admin
from sito.models import *
from image_cropping import ImageCroppingMixin

def get_fiera(self):
    fiera = "null"
    if self.fiera:
        fiera = self.fiera.titolo
        return fiera
    else:
        return fiera

def get_provincia(self):
	if self.provincia:
		return self.provincia.titolo
	else:
		return ""

class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


class SliderAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_img", "titolo", "active")


class FiereAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_img", "titolo", get_provincia, "location", "attiva_slider", "active")


class StandAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_img", "titolo", get_provincia, "azienda", get_fiera, "attiva_slider", "active")


class ShowroomAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_img", "titolo", get_provincia, "azienda", "attiva_slider", "active")


admin.site.register(Slider, SliderAdmin)
admin.site.register(Province, MyModelAdmin)
admin.site.register(Fiere, FiereAdmin)
admin.site.register(Stand, StandAdmin)
admin.site.register(Showroom, ShowroomAdmin)
admin.site.register(Casehistory, ShowroomAdmin)
admin.site.register(Gallery, SliderAdmin)



