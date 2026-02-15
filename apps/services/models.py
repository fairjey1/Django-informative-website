from django.db import models

# Create your models here.

class Service(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='services/')
    icono = models.CharField(max_length=50, help_text="Clase de FontAwesome (ej: fa-code)", default="fa-gear") 
    orden = models.IntegerField(default=0, help_text="Para decidir cuál va primero")
    activo = models.BooleanField(default=True)
    precio = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['orden']

    def __str__(self):
        return self.titulo

class ServiceImage(models.Model):
    servicio = models.ForeignKey('services.Service', on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='service_images/')
    def __str__(self):
        return f"Imagen para {self.servicio.titulo}"
    

class ServiceFAQ(models.Model):
    servicio = models.ForeignKey('services.Service', on_delete=models.CASCADE, related_name='faqs')
    pregunta = models.CharField(max_length=255)
    respuesta = models.TextField()

    def __str__(self):
        return f"FAQ para {self.servicio.titulo}: {self.pregunta}"