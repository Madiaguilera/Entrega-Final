""" 
from django.contrib import admin
from .models import JabonFrutal, JabonFloral, JabonPlayero
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Configuración para JabonFrutal
@admin.register(JabonFrutal)
class JabonFrutalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cantidad')
    list_filter = ('precio',)
    search_fields = ('nombre',)
    list_editable = ('precio', 'cantidad')

# Configuración para JabonFloral  
@admin.register(JabonFloral)
class JabonFloralAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cantidad')
    list_filter = ('precio',)
    search_fields = ('nombre',)
    list_editable = ('precio', 'cantidad')

# Configuración para JabonPlayero
@admin.register(JabonPlayero)
class JabonPlayeroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cantidad')
    list_filter = ('precio',)
    search_fields = ('nombre',)
    list_editable = ('precio', 'cantidad')


class UserAdmin(BaseUserAdmin): 
    # Define las columnas que se mostrarán en la lista de usuarios en el panel de administración de Django. 
    # En este caso, se mostrarán: nombre de usuario, email, nombre, apellido
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    # Permite buscar usuarios en el panel de administración usando los campos especificados (nombre de usuario, nombre, apellido y email)
    search_fields = ('username', 'first_name', 'last_name', 'email')
    # Hace que los campos listados sean de solo lectura en el formulario de edición del usuario
    readonly_fields = ('date_joined', 'last_login')
    # Organiza los campos del formulario de edición en secciones
    fieldsets = (
        ('Usuario - Contraseña', {'fields': ('username', 'password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    ) 
admin.site.unregister(User) 
admin.site.register(User, UserAdmin)

# Personalizar el panel de administración
admin.site.site_header = "Ecosmetic Inventario - Administración"
admin.site.site_title = "Ecosmetic Admin"
admin.site.index_title = "Panel de Control del Inventario"


class UserAdmin(BaseUserAdmin):
     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
     search_fields = ('username', 'first_name', 'last_name', 'email')
     readonly_fields = ('date_joined', 'last_login')
     fieldsets = (
         ('Usuario - Contraseña', {'fields': ('username', 'password',)}),
         ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
         ('Important dates', {'fields': ('last_login', 'date_joined')}),
     )

    """
from django.contrib import admin
from .models import JabonFrutal, JabonFloral, JabonPlayero

# Registro simple sin personalizaciones
admin.site.register(JabonFrutal)
admin.site.register(JabonFloral)
admin.site.register(JabonPlayero)

# Personalización básica del sitio
admin.site.site_header = "Ecosmetic Inventario"
admin.site.site_title = "Ecosmetic Admin"
admin.site.index_title = "Panel de Control"