from django.db import models

# Create your models here.

# apps/core/models.py
from django.db import models

class SiteConfiguration(models.Model): 
    '''Modelo para almacenar la configuración global del sitio web. Esto permite al usuario cambiar ciertos parámetros desde el panel de administración'''
    
    nombre_sitio = models.CharField(max_length=100, default="Mi Empresa")
    logo = models.ImageField(upload_to="config/", blank=True, null=True)
    email_contacto = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.TextField(blank=True)
    
    # Redes Sociales
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    
    # Sección de ubicación
    ubicacion_titulo = models.CharField(max_length=100, default="Nuestra Ubicación", help_text="Ej: Cómo llegar, Dónde estamos")
    ubicacion_texto = models.TextField(blank=True, help_text="Instrucciones escritas (Ej: 'Frente a la plaza...')")
    mapa_embed = models.TextField(blank=True, verbose_name="Código del Mapa (Google Maps)", help_text="Pega aca el código embed de Google Maps")

    class Meta:
        verbose_name = "Configuración del Sitio"
        verbose_name_plural = "Configuraciones"

    def save(self, *args, **kwargs):
        '''Funcion para asegurar el singleton del modelo'''
        self.pk = 1
        super(SiteConfiguration, self).save(*args, **kwargs) # Asegura que solo haya una instancia 

    def __str__(self):
        return "Configuración Global"
