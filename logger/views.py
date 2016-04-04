from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from models import *


class InvestigationList(ListView):
    model = Investigation


class InvestigationDetail(DetailView):
    model = Investigation


class InvestigationCreate(CreateView):
    model = Investigation
    fields = '__all__'


class InvestigationUpdate(UpdateView):
    model = Investigation
    fields = '__all__'


class InvestigationDelete(DeleteView):
    model = Investigation
    success_url = reverse_lazy('index')
