from django.shortcuts import render
from Ecosmetic_Inventario.forms import JabonFloralForm 
from Ecosmetic_Inventario.forms import JabonFloral


def LeerJabonFloral(request):
    jabon = JabonFloral.objects.all()
    return render(request, "Ecosmetic_Inventario/formulario/LeerJabonFloral.html", {"JabonFloral": jabon})

def agregar_jabon_floral(request):
    if request.method == "POST":
        form = JabonFloralForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            jabon = JabonFloral(
                nombre = info["nombre"],
                precio = info["precio"],
                cantidad = info["cantidad"]
            )
            jabon.save()
            return render(request, "Ecosmetic_Inventario/inicio.html")
    else:
        form = JabonFloralForm()
    
    return render(request, "Ecosmetic_Inventario/formulario/jabon_floral_formulario.html", {"form": form})

def EliminarJabonFloral(request,id_jabon):
    jabon= JabonFloral.objects.get(id=id_jabon)
    jabon.delete()
    return LeerJabonFloral(request)
    
def EditarJabonFloral(request, id_jabon):
    jabon = JabonFloral.objects.get(id=id_jabon)
    if request.method == "POST":
        form = JabonFloralForm(request.post)
        if form.is_valid():
            info = form.cleaned_data
            jabon.nombre = info["nombre"]
            jabon.precio = info["precio"]
            jabon.cantidad= info ["cantidad"]
            jabon.save()
            return LeerJabonFloral(request)
    else:
        form = JabonFloralForm(
            initial={
            'nombre': jabon.nombre, 
            'precio': jabon.precio,
            'cantidad': jabon.cantidad    
            }
        )
        
    return render (request, "Ecosmetic_Inventario/formulario/editarjabonfloral.html", {"Formulario": form, "jabon_id":jabon.id})

