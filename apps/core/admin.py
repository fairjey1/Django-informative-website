from django.contrib import admin

# Register your models here.
from .models import SiteConfiguration

@admin.register(SiteConfiguration) 
class SiteConfigurationAdmin(admin.ModelAdmin):
    # Evitamos que el usuario pueda añadir más de uno o borrarlo
    def has_add_permission(self, request):
        return False if SiteConfiguration.objects.exists() else True

    def has_delete_permission(self, request, obj=None):
        return False