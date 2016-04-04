from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models


class Investigation(models.Model):
    title = models.CharField(max_length=32)
    opened = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False)
    question = models.CharField(max_length=128)
    discussion = models.TextField(blank=True)
    shelved = models.BooleanField(default=False)
    related = models.ManyToManyField('self', blank=True, symmetrical=False)

    def get_absolute_url(self):
        return reverse('investigation-detail', kwargs={'pk': self.pk})
