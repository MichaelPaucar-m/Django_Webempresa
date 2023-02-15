from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from.forms import ContactForm
from django.urls import reverse

# Create your views here.
def contact (request): 
    contactForm= ContactForm ()
    #instanciar la clase del formulario 
    #print("Tipo de peticion: {}".format(request.method))
    if request.method =="POST":
        contactForm=ContactForm(data=request.POST)
        if contactForm.is_valid(): 
            name=request.POST.get('name','')
            email=request.POST.get('email','') 
            content=request.POST.get('content','')
            email=EmailMessage(
                "La caffetiera: Nuevo mensaje de contacto",
                "de {} <{}> \n\nEscribio:\n\n{}".format(name, email, content),
                "", 
                ["vflores"],
                reply_to={email} 
            )
            try: 
                  email.send()
                  return redirect(reverse('contact')+"?ok")
            except: 
                  return redirect(reverse('contact')+"?faild")
    return render (request, "contact/contact.html", {'form': contactForm})