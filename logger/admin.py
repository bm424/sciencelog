# Register your models here.
from django.contrib import admin

from logger import models, forms


class ImageInline(admin.TabularInline):
    model = models.Image
    fields = ["image_path"]


class InvestigationAdmin(admin.ModelAdmin):
    form = forms.InvestigationForm


class LogAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(models.Investigation, InvestigationAdmin)
admin.site.register(models.Log, LogAdmin)
admin.site.register(models.Image)

