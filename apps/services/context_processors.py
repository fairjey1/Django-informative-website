from .models import Service

def services_processor(request):
    # Traemos los primeros 5 servicios activos para el menú
    return {
        'servicios_nav': Service.objects.filter(activo=True)[:5]
    }