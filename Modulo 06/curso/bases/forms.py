from django import forms
from .models import Tarea


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ("titulo", "descripcion", "fecha_inicio", "fecha_limite")

        widgets = {
            "titulo": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Título",
            }),

            "descripcion": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Descripción",
            }),

            "fecha_inicio": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                },
            ),

            "fecha_limite": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                },
            ),
        }
    
    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data['fecha_inicio'] > cleaned_data['fecha_limite']:
            raise forms.ValidationError("La fecha de inicio no puede ser mayor a la fecha límite")
        
        return cleaned_data
