from django import forms
from django.utils.text import slugify

from . import models


class InvestigationForm(forms.ModelForm):
    class Meta:
        model = models.Investigation
        fields = '__all__'

    def save(self, commit=True):
        instance = super(InvestigationForm, self).save(commit=False)
        instance.slug = slugify(instance.title)
        instance.save()
        return instance


class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = '__all__'

    def save(self, commit=True):
        instance = super(ImageForm, self).save(commit=False)
        instance.slug = slugify(instance.title)
        instance.save()
        return instance


