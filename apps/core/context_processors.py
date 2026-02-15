from .models import SiteConfiguration

def site_info(request):
    '''Context processor para agregar la configuración del sitio a todas las plantillas'''
    config, created = SiteConfiguration.objects.get_or_create(pk=1) # Asegura obtener la única instancia
    return {
        'sitio': config # luego llamo con sitio.logo, sitio.nombre_sitio, etc.
    }