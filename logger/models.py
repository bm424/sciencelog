from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models


class Investigation(models.Model):
    title = models.CharField(max_length=32)
    opened = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False)
    question = models.CharField(max_length=128)
    hypothesis = models.TextField(blank=True)
    shelved = models.BooleanField(default=False)
    related = models.ManyToManyField('self', blank=True, symmetrical=False)
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('investigation-detail', kwargs={'slug': self.slug})


class Log(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_edit = models.DateTimeField(auto_now=True, editable=False)
    summary = models.CharField(max_length=256)
    investigation = models.ForeignKey(Investigation, limit_choices_to={
        'shelved': False})
    text = models.TextField()

    class Meta:
        ordering = ['-last_edit']

    def __str__(self):
        return self.created.strftime("%Y/%m/%d %H:%M")

    def get_absolute_url(self):
        return reverse('investigation-logs-detail', kwargs={'slug':
                                                      self.investigation.slug, 'pk':self.pk})


class Image(models.Model):
    log = models.ForeignKey(Log)
    image_path = models.ImageField(upload_to="images/%Y/%m/%d")
    title = models.CharField(max_length=32)
    caption = models.TextField()
    url = models.CharField("Url", max_length=128, blank=True)

    def __str__(self):
        if self.pk is not None:
            return "{{{{ {} }}}}".format(self.pk)
        else:
            return "deleted image"




