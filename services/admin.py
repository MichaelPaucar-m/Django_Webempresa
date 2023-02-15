from django.contrib import admin
from .models import Services
# Register your models here.
#para mostrar configuraciones extendidas del administrador 

class ServicesAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated') 


admin.site.register(Services, ServicesAdmin)
