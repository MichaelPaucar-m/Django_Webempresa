from .models import Link

def ctx_dict(request): 
    ctx={}
    #cargar lalista de redes sociales 
    link=Link.objects.all()
    #agregamos dentro del diccionarion
    for link in links:
        ctx[link.key]= link.url #llenamos el diccionario
    return ctx 