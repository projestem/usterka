from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from zgloszenia.models import Zgloszenie


def index(request):
    return render(request,'zgloszenia/index.html')

class UtworzZgloszenie(SuccessMessageMixin,CreateView):
    model = Zgloszenie
    fields = ['opis', 'miejsce', 'imie', 'nazwisko']
    success_url = reverse_lazy('zgloszenia:index')
    success_message = 'Dodano zgłoszenie!'