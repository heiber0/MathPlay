# En tu archivo forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# 1. Formulario de Inicio de Sesión


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Iterar sobre los campos y añadir placeholder y clase
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Nombre de usuario',
            'class': 'auth-input'  # Clase para aplicar estilos comunes si es necesario
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Contraseña',
            'class': 'auth-input'
        })
        # Opcionalmente, ocultar la etiqueta para que solo se vea el placeholder
        self.fields['username'].label = False
        self.fields['password'].label = False


# 2. Formulario de Registro (¡Ajuste aquí!)
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        # Es crucial llamar a super().__init__ primero para que los campos existan
        super().__init__(*args, **kwargs)

        # Mapeo de placeholders para UserCreationForm
        # Usamos los nombres correctos de los campos: username, password_1, password_2
        # Los nombres son 'username', 'password_1', 'password_2'

        # Lista de campos que queremos personalizar
        field_customizations = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña'
        }

        for field_name, placeholder_text in field_customizations.items():
            # Intentar acceder al campo solo si existe
            if field_name in self.fields:
                self.fields[field_name].widget.attrs.update({
                    'placeholder': placeholder_text,
                    'class': 'auth-input'
                })
                # Ocultar la etiqueta
                self.fields[field_name].label = False

            # Nota: Los campos de password_1 y password_2 deberían existir
            # Si el error persiste, verifica la versión de Django o los nombres exactos
