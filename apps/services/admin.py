from django.contrib import admin

# Register your models here.
from .models import Service, ServiceFAQ, ServiceImage


# Creamos una vista en línea (Inline)
class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1 # Cuántos campos vacíos mostrar por defecto

class ServiceFAQInline(admin.TabularInline):
    model = ServiceFAQ
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden', 'activo', 'precio') 
    prepopulated_fields = {'slug': ('titulo',)} # Genera el slug automáticamente
    inlines = [ServiceImageInline, ServiceFAQInline] # Permite agregar imágenes y FAQs directamente desde la página del servicio

