from django import forms
from django.contrib.auth.forms import UserCreationForm

class CrearUsuarioForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget = forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Usuario",
        })

        self.fields["password1"].widget = forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Contraseña",
        })

        self.fields["password2"].widget = forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Confirmar contraseña",
        })

