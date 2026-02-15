import os
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from config import settings
from .models import ContactMessage
from .forms import ContactForm

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

class ContactCreateView(CreateView):
    model = ContactMessage
    form_class = ContactForm
    template_name = 'contact/contact_form.html'
    success_url = reverse_lazy('contact_success') # mensaje de exito después de enviar el formulario

    def form_valid(self, form):
        #guardar mensaje en la bd
        response = super().form_valid(form)

        # lógica para enviar un email 
        nombre = form.cleaned_data['nombre']
        email_cliente = form.cleaned_data['email']
        asunto = form.cleaned_data['asunto']
        mensaje = form.cleaned_data['mensaje']

        # Creamos un contexto para pasarle variables al template del email
        context = {
            'nombre': nombre,
            'email': email_cliente,
            'mensaje': mensaje,
        }   
        
        # Renderizamos el template del email con el contexto
        html_content = render_to_string('contact/emails/new_message.html', context)
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            subject=f"Nueva consulta web: {asunto}",
            body=text_content, # Versión texto plano
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[os.getenv('EMAIL_RECIPIENT')], # A quién le llega (al dueño)
            reply_to=[email_cliente] # Para que al dar "Responder" le escribas al cliente
        )

        email.attach_alternative(html_content, "text/html") # Adjuntamos la versión HTML del email
        
        try:
            email.send()
            messages.success(self.request, "¡Gracias! Tu mensaje ha sido enviado correctamente.")
        except Exception as e:
            print(f"Error enviando correo: {e}")

        return response
