from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Service
from django.views.generic import DetailView

class ServiceListView(ListView):
    model = Service
    template_name = 'services/list.html'
    context_object_name = 'servicios' # Así lo llamaremos en el HTML

    def get_queryset(self):
        return Service.objects.filter(activo=True)
    
class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/detail.html'
    context_object_name = 'servicio'