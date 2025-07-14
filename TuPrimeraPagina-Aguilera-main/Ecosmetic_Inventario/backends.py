from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

class AnyCredentialsBackend(BaseBackend):
    """
    Backend de autenticación personalizado que acepta cualquier combinación 
    de usuario y contraseña para fines de desarrollo/aprendizaje.
    """
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username and password:
            # Buscar si el usuario ya existe
            try:
                user = User.objects.get(username=username)
                return user
            except User.DoesNotExist:
                # Si no existe, crear un nuevo usuario
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    is_staff=True,  # Darle permisos de staff
                    is_superuser=True  # Darle permisos de superusuario
                )
                return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
