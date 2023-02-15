from django.db import models

# Create your models here.
#tabla 
class Services(models.Model):
    title=models.CharField(max_length=200, verbose_name="titulo")
    subtitle=models.CharField(max_length=200, verbose_name="Subtitulo")
    content=models.TextField(verbose_name="Contenido")
    image=models.ImageField(verbose_name="Imagen", upload_to="services")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta: 
        verbose_name="servicio"
        verbose_name_plural="servicios"
        ordering=['-created']
    
    def _str_(self): 
        return self.title 



