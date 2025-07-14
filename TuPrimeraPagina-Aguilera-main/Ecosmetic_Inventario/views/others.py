from django.shortcuts import render, redirect
from ..models import JabonFrutal, JabonFloral, JabonPlayero
from django.contrib import messages
from ..forms import JabonFrutalForm, JabonFloralForm, JabonPlayeroForm, BusquedaForm
from django.http import HttpResponse


def inicio(request):
    # Calculamos estadísticas para el dashboard
    total_jabones_frutales = JabonFrutal.objects.count()
    total_jabones_florales = JabonFloral.objects.count()
    total_jabones_playeros = JabonPlayero.objects.count()
    total_productos = total_jabones_frutales + total_jabones_florales + total_jabones_playeros
    
    context = {
        'total_productos': total_productos,
        'total_jabones_frutales': total_jabones_frutales,
        'total_jabones_florales': total_jabones_florales,
        'total_jabones_playeros': total_jabones_playeros,
    }
    return render(request, "Ecosmetic_Inventario/dashboard.html", context)

def listar_jabones_frutales(request):
    jabones = JabonFrutal.objects.all()
    return render(request, "Ecosmetic_Inventario/productos.html", {'jabones': jabones, 'tipo': 'frutales'})

def listar_jabones_florales(request):
    jabones = JabonFloral.objects.all()
    return render(request, "Ecosmetic_Inventario/productos.html", {'jabones': jabones, 'tipo': 'florales'})

def listar_jabones_playeros(request):
    jabones = JabonPlayero.objects.all()
    return render(request, "Ecosmetic_Inventario/productos.html", {'jabones': jabones, 'tipo': 'playeros'})

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
            messages.success(request, 'Jabón frutal agregado exitosamente')
            return redirect('inicio')
    else:
        form = JabonFrutalForm()
    
    return render(request, "Ecosmetic_Inventario/formulario/jabon_frutal_formulario.html", {"form": form})

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
            messages.success(request, 'Jabón floral agregado exitosamente')
            return redirect('inicio')
    else:
        form = JabonFloralForm()
    
    return render(request, "Ecosmetic_Inventario/formulario/jabon_floral_formulario.html", {"form": form})

def agregar_jabon_playero(request):
    if request.method == "POST":
        form = JabonPlayeroForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            jabon = JabonPlayero(
                nombre = info["nombre"],
                precio = info["precio"],
                cantidad = info["cantidad"]
            )
            jabon.save()
            messages.success(request, 'Jabón playero agregado exitosamente')
            return redirect('inicio')
    else:
        form = JabonPlayeroForm()
    
    return render(request, "Ecosmetic_Inventario/formulario/jabon_playero_formulario.html", {"form": form})

def busqueda_jabon(request):
    form = BusquedaForm()
    return render(request, "Ecosmetic_Inventario/formulario/busquedaCamada.html", {"form": form})

def buscar_jabon(request):
    if request.GET.get("id"):
        jabon_id = request.GET["id"]
        jabon_encontrado = None
        tipo_jabon = ""
        
        # Buscamos en los tres tipos de jabones
        try:
            jabon_encontrado = JabonFrutal.objects.get(id=jabon_id)
            tipo_jabon = "Frutal"
        except JabonFrutal.DoesNotExist:
            try:
                jabon_encontrado = JabonFloral.objects.get(id=jabon_id)
                tipo_jabon = "Floral"
            except JabonFloral.DoesNotExist:
                try:
                    jabon_encontrado = JabonPlayero.objects.get(id=jabon_id)
                    tipo_jabon = "Playero"
                except JabonPlayero.DoesNotExist:
                    pass
        
        # Si se encuentra el jabón
        if jabon_encontrado:
            # Determinar el estado del stock
            if jabon_encontrado.cantidad > 10:
                estado_stock = "Alto"
                clase_stock = "success"
            elif jabon_encontrado.cantidad > 5:
                estado_stock = "Medio"
                clase_stock = "warning"
            else:
                estado_stock = "Bajo"
                clase_stock = "danger"
            
            context = {
                'jabon': jabon_encontrado,
                'tipo_jabon': tipo_jabon,
                'id_buscado': jabon_id,
                'estado_stock': estado_stock,
                'clase_stock': clase_stock,
                'encontrado': True
            }
            return render(request, "Ecosmetic_Inventario/formulario/resultadosBusqueda.html", context)
        else:
            messages.error(request, f"No se encontró ningún jabón con el ID: {jabon_id}")
            return redirect('busqueda_jabon')
    else:
        messages.error(request, "No enviaste ningún ID válido.")
        return redirect('busqueda_jabon')

def informacion_acceso(request):
    """Vista que muestra información sobre cómo acceder al admin"""
    return render(request, "Ecosmetic_Inventario/info_acceso.html")

