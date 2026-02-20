# Web de informativa en Django 🚀
Este es un proyecto web full-stack que desarrollé para poner en práctica mis conocimientos de backend. Está pensado como una web informativa para ofrecer servicios (actualmente configurado para un negocio genérico), pero su arquitectura es escalable para otros rubros.

## 🛠️ Tecnologías que usé

* **Backend:** Python + Django 5
* **Base de Datos:** PostgreSQL (en producción) / SQLite (en desarrollo)
* **Almacenamiento Multimedia:** Cloudinary. Lo implementé para guardar las fotos de los servicios directamente en la nube
* **Envío de Emails:** API de Resend. Configurado para el formulario de contacto usando HTTPS.
* **Despliegue y Servidor:** Railway, usando Gunicorn y WhiteNoise para servir los archivos estáticos

## ⚙️ Características Principales

* Panel de administración de Django configurado para gestionar casi toda la web
* Formulario de contacto 
* Diseño responsive
