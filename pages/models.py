from django.db import models 
from ckeditor.fields import RichTextField

# Create your models here.
class Page (models.Model): 
    title= models.CharField (verbose_name='Titulo', max_length=200)
    content= RichTextField(verbose_name ="Contenido")
    created=models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creacion")
    updated= models.DateTimeField(
        auto_now=True, verbose_name="fecha de edicion")
    
    class Meta: 
        verbose_name= "pagina"
        verbose_name_plural ="paginas"
        ordering= ['title']
    
    def _str_ (self): 
        return self.title