from django.forms import ModelForm
from .models import Tarea

class formularioTareas(ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo','descripcion','urgente']
