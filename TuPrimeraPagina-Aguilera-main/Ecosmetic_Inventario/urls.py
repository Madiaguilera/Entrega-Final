from django.urls import path

from Ecosmetic_Inventario.views.others import (
    inicio,
    listar_jabones_frutales,
    listar_jabones_florales,
    listar_jabones_playeros,
    agregar_jabon_frutal,
    agregar_jabon_floral,
    agregar_jabon_playero,
    busqueda_jabon,
    buscar_jabon,
    informacion_acceso
)

from Ecosmetic_Inventario.views.JabonFrutal import LeerJabonFrutal, EliminarJabonFrutal, EditarJabonFrutal
from Ecosmetic_Inventario.views.JabonFloral import LeerJabonFloral, EliminarJabonFloral, EditarJabonFloral
from Ecosmetic_Inventario.views.JabonPlayero import (
    JabonPlayeroListView,  
    JabonPlayeroCreateView,  
    JabonPlayeroUpdateView, 
    JabonPlayeroDeleteView
)

urlpatterns = [
    # URL principal
    path('', inicio, name='inicio'),
    
    # SOLUCIÓN TEMPORAL: Agregar la URL 'frutal' que apunte a la misma vista
    path('frutal/', inicio, name='frutal'),
    
    # URLs para listar jabones
    path('jabones-frutales/', listar_jabones_frutales, name='listar_jabones_frutales'),
    path('jabones-florales/', listar_jabones_florales, name='listar_jabones_florales'),
    path('jabones-playeros/', listar_jabones_playeros, name='listar_jabones_playeros'),
    
    # URLs para agregar jabones
    path('jabon-frutal-formulario/', agregar_jabon_frutal, name='agregar_jabon_frutal'),
    path('jabon-floral-formulario/', agregar_jabon_floral, name='agregar_jabon_floral'),
    #path('jabon-playero-formulario/', agregar_jabon_playero, name='agregar_jabon_playero'),
    
    # URLs adicionales para compatibilidad con templates
    path('formulario-frutal/', agregar_jabon_frutal, name='formulario_frutal'),
    path('formulario-floral/', agregar_jabon_floral, name='formulario_floral'),
    path('formulario-playero/', agregar_jabon_playero, name='formulario_playero'),
    
       # URLs para búsqueda
    path('busqueda-jabon/', busqueda_jabon, name='busqueda_jabon'),
    path('buscar/', buscar_jabon, name='buscar'),
    path('info-acceso/', informacion_acceso, name='informacion_acceso'),
    
    # URLs para jabones frutales
    path('leer-jabon-frutal/', LeerJabonFrutal, name='leer_jabon_frutal'),
    path('eliminar-jabon-frutal/<int:id_jabon>/', EliminarJabonFrutal, name='eliminar_jabon_frutal'),
    path('editar-jabon-frutal/<int:id_jabon>/', EditarJabonFrutal, name='editar_jabon_frutal'),
    
    # URLs para jabones florales
    path('leer-jabon-floral/', LeerJabonFloral, name='leer_jabon_floral'),
    path('eliminar-jabon-floral/<int:id_jabon>/', EliminarJabonFloral, name='eliminar_jabon_floral'),
    path('editar-jabon-floral/<int:id_jabon>/', EditarJabonFloral, name='editar_jabon_floral'),
    
    # URLs para jabones playeros
    path('JabonPlayero/', JabonPlayeroListView.as_view(), name='JabonPlayero'),
    path('JabonPlayero/<int:pk>/', JabonPlayeroDeleteView.as_view(), name='JabonPlayero_detail'),  # Corregido
    path('JabonPlayero/nuevo/', JabonPlayeroCreateView.as_view(), name='JabonPlayero_new'), 
    path('JabonPlayero/editar/<int:pk>/', JabonPlayeroUpdateView.as_view(), name='JabonPlayero_edit'),
    path('JabonPlayero/borrar/<int:pk>/', JabonPlayeroDeleteView.as_view(), name='JabonPlayero_delete'),

]