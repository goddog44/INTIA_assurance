from django.shortcuts import render # type: ignore
from django.views.generic import ListView, CreateView, UpdateView, DeleteView # type: ignore
from django.urls import reverse_lazy # type: ignore
from .models import Client
from .forms import ClientForm # type: ignore

class ClientListView(ListView):
    model = Client
    template_name = 'clients/list.html'
    context_object_name = 'clients'

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/form.html'
    
    def get_success_url(self):
        return reverse_lazy('clients:list')

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/form.html'
    
    def get_success_url(self):
        return reverse_lazy('clients:list')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'partials/delete_confirm.html'
    
    def get_success_url(self):
        return reverse_lazy('clients:list')