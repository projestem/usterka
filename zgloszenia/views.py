from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView

from zgloszenia.models import Zgloszenie


def index(request):
    return render(request, 'zgloszenia/index.html')


class UtworzZgloszenie(SuccessMessageMixin, CreateView):
    model = Zgloszenie
    fields = ['opis', 'miejsce', 'imie', 'nazwisko']
    success_url = reverse_lazy('zgloszenia:index')
    success_message = 'Dodano zgłoszenie!'

class ListaZgloszen(ListView):
    model = Zgloszenie

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ListaZgloszen,self).dispatch(request,*args,**kwargs)

class UsunZgloszenie(DeleteView):
    model = Zgloszenie
    success_url = reverse_lazy('zgloszenia:lista')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UsunZgloszenie, self).dispatch(request, *args, **kwargs)