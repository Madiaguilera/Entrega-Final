from django.views.generic import ListView  # Importamos ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from Ecosmetic_Inventario.models import JabonPlayero


class JabonPlayeroListView(ListView):
    """
    Vista para listar todos los jabones playeros.
    """
    model = JabonPlayero
    template_name = 'Ecosmetic_Inventario/JabonPlayero/JabonPlayero_list.html'
    paginate_by = 10 
    ordering = ['nombre'] 
    context_object_name = 'jabones'


class JabonPlayeroDetailView(DetailView):
    """
    Vista para mostrar los detalles de un jabón playero específico.
    """
    model = JabonPlayero
    template_name = 'Ecosmetic_Inventario/JabonPlayero/JabonPlayero_detail.html'


class JabonPlayeroCreateView(CreateView):
    """
    Vista para crear un nuevo jabón playero.
    """
    model = JabonPlayero
    fields = ['nombre', 'precio', 'cantidad']
    template_name = 'Ecosmetic_Inventario/JabonPlayero/JabonPlayero_form.html'
    success_url = reverse_lazy('JabonPlayero')

class JabonPlayeroUpdateView(UpdateView):
    """
    Vista para editar un jabón playero existente.
    """
    model = JabonPlayero
    fields = ['nombre', 'precio', 'cantidad']
    template_name = 'Ecosmetic_Inventario/JabonPlayero/JabonPlayero_form.html'
    success_url = reverse_lazy('JabonPlayero')

class JabonPlayeroDeleteView(DeleteView):
    """Vista para eliminar un jabón playero existente.
    """ 
    model = JabonPlayero
    template_name = 'Ecosmetic_Inventario/JabonPlayero/JabonPlayero_confirm_delete.html'
    success_url = reverse_lazy('JabonPlayero') 