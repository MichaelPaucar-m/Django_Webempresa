from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User # creador de los usuarios
from tabnanny import verbose

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200, verbose_name="Nombre")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated= models.DateTimeField(
        auto_now=True, verbose_name="fecha de edicion")

    class Meta: 
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["-created"] 
    
    def _str_(self):
        return self.name

class Blog(models.Model): 
    title= models.CharField(max_length=200, verbose_name="Titulo")
    content=models.TextField(verbose_name="Contenido")
    published=models.DateTimeField(verbose_name="Fecha de publicacion", default=now)
    image=models.ImageField(verbose_name="Imagen", upload_to="blogs")
    #algo nuevoooooooooooooo Trae desde la clase author y permite borrar todo de un usuario
    author=models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories=models.ManyToManyField(Category, verbose_name="Categorias")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated= models.DateTimeField(
        auto_now=True, verbose_name="fecha de edicion")
    
    class Meta: 
        verbose_name="Entrada"
        verbose_name_plural="Entradas"
        ordering = ["-created"]
    
    def _str_(self): 
        return self.title