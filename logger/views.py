from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.utils.text import slugify

from logger import models
from logger import forms


class InvestigationList(ListView):
    queryset = models.Investigation.objects.all().filter(shelved=False)
    context_object_name = 'investigations'
    ordering = '-opened'


class InvestigationDetail(DetailView):
    model = models.Investigation
    context_object_name = 'investigation'


class InvestigationCreate(CreateView):
    model = models.Investigation
    fields = '__all__'

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super(InvestigationCreate, self).form_valid(form)


class InvestigationUpdate(UpdateView):
    model = models.Investigation
    fields = '__all__'


class InvestigationDelete(DeleteView):
    model = models.Investigation
    success_url = reverse_lazy('index')


class LogList(ListView):
    model = models.Log
    context_object_name = 'logs'
    ordering = '-created'

    def get_queryset(self):
        if self.kwargs:
            investigation = models.Investigation.objects.get(
                slug=self.kwargs['slug'])
            return self.model.objects.filter(investigation=investigation)
        else:
            return self.model.objects.all()


class LogCreate(CreateView):
    model = models.Log
    fields = '__all__'

    def get_initial(self):
        initial = super(LogCreate, self).get_initial()
        if self.kwargs:
            investigation = models.Investigation.objects.get(
                slug=self.kwargs['slug'])
            initial['investigation'] = investigation.pk
        return initial


class LogUpdate(UpdateView):
    model = models.Log
    fields = '__all__'

    def get_object(self, queryset=None):
        obj = models.Log.objects.get(pk=self.kwargs['pk'])
        return obj


class LogDetail(DetailView):
    model = models.Log
    context_object_name = 'log'


class ImageList(ListView):
    model = models.Image
    context_object_name = 'image'



