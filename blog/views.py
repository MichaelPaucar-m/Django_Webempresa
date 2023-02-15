from django.shortcuts import render, get_object_or_404
from .models import Blog, Category
# Create your views here. 


def blog (request): 
    #consultas 
    blogs= Blog.objects.all()
    return render (request, "blog/blog.html",{'blogs': blogs})

#obtener el id y direccion url
def category(request, category_id):
   # pass#hace que no se caiga el programa si esta imcompleto 
   category=get_object_or_404(Category, id=category_id)
   #tomar los blogs que le pertencen a esta categoria 
   blogs=Blog.objects.filter(categories=category)
   return render (request, "blog/category.html",{'blogs': blogs})