from django.contrib import admin

from .models import Tarea

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha_creacion",)



admin.site.register(Tarea, TaskAdmin)