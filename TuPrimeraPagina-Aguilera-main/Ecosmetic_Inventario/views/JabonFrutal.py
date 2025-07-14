from django.shortcuts import render
from Ecosmetic_Inventario.forms import JabonFrutalForm
from Ecosmetic_Inventario.forms import JabonFrutal

def LeerJabonFrutal(request):
    jabon = JabonFrutal.objects.all()
    return render(request, "Ecosmetic_Inventario/formulario/LeerJabonFrutal.html", {"JabonFrutal": jabon})

def agregar_jabon_frutal(request):
    if request.method == "POST":
        form = JabonFrutalForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            jabon = JabonFrutal(
                nombre = info["nombre"],
                precio = info["precio"],
                cantidad = info["cantidad"]
            )
            jabon.save()
            return render(request, "Ecosmetic_Inventario/inicio.html")
    else:
        form = JabonFrutalForm()
    
    return render(request, "Ecosmetic_Inventario/formulario/jabon_frutal_formulario.html", {"form": form})

def EliminarJabonFrutal(request,id_jabon):
    jabon= JabonFrutal.objects.get(id=id_jabon)
    jabon.delete()
    return LeerJabonFrutal(request)

def EditarJabonFrutal(request, id_jabon):
    jabon = JabonFrutal.objects.get(id=id_jabon)
    if request.method == "POST":
        form = JabonFrutalForm(request.post)
        if form.is_valid():
            info = form.cleaned_data
            jabon.nombre = info["nombre"]
            jabon.precio = info["precio"]
            jabon.cantidad= info ["cantidad"]
            jabon.save()
            return LeerJabonFrutal(request)
    else:
        form = JabonFrutalForm(
            initial={
            'nombre': jabon.nombre, 
            'precio': jabon.precio,
            'cantidad': jabon.cantidad    
            }
        )
        
    return render (request, "Ecosmetic_Inventario/formulario/editarjabonfrutal.html", {"Formulario": form, "jabon_id":jabon.id})