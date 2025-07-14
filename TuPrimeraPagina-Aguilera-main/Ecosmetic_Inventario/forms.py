from django import forms
from .models import JabonFrutal, JabonFloral, JabonPlayero
from django.core.exceptions import ValidationError

class JabonFrutalForm(forms.ModelForm):
    class Meta:
        model = JabonFrutal
        fields = ['nombre', 'precio', 'cantidad']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre del jabón frutal',
                'required': True
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control', 
                'step': '0.01', 
                'placeholder': 'Precio (ej: 15.99)',
                'min': '0.01',
                'required': True
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Cantidad en stock',
                'min': '0',
                'required': True
            })
        }
        labels = {
            'nombre': 'Nombre del Jabón',
            'precio': 'Precio ($)',
            'cantidad': 'Cantidad en Stock'
        }
    
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio and precio <= 0:
            raise ValidationError("El precio debe ser mayor a cero.")
        return precio
    
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad and cantidad < 0:
            raise ValidationError("La cantidad no puede ser negativa.")
        return cantidad

class JabonFloralForm(forms.ModelForm):
    class Meta:
        model = JabonFloral
        fields = ['nombre', 'precio', 'cantidad']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre del jabón floral',
                'required': True
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control', 
                'step': '0.01', 
                'placeholder': 'Precio (ej: 15.99)',
                'min': '0.01',
                'required': True
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Cantidad en stock',
                'min': '0',
                'required': True
            })
        }
        labels = {
            'nombre': 'Nombre del Jabón',
            'precio': 'Precio ($)',
            'cantidad': 'Cantidad en Stock'
        }
    
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio and precio <= 0:
            raise ValidationError("El precio debe ser mayor a cero.")
        return precio
    
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad and cantidad < 0:
            raise ValidationError("La cantidad no puede ser negativa.")
        return cantidad

class JabonPlayeroForm(forms.ModelForm):
    class Meta:
        model = JabonPlayero
        fields = ['nombre', 'precio', 'cantidad']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre del jabón playero',
                'required': True
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control', 
                'step': '0.01', 
                'placeholder': 'Precio (ej: 15.99)',
                'min': '0.01',
                'required': True
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Cantidad en stock',
                'min': '0',
                'required': True
            })
        }
        labels = {
            'nombre': 'Nombre del Jabón',
            'precio': 'Precio ($)',
            'cantidad': 'Cantidad en Stock'
        }
    
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio and precio <= 0:
            raise ValidationError("El precio debe ser mayor a cero.")
        return precio
    
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad and cantidad < 0:
            raise ValidationError("La cantidad no puede ser negativa.")
        return cantidad

class BusquedaForm(forms.Form):
    id = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el ID del jabón'
        }),
        label='ID del Jabón'
    )