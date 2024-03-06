"""
URL configuration for crud_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from . import views

LOGIN_URL='login'
LOGIN_REDIRECT_URL='login'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', views.registro, name='registro'),
    path('tareas/', views.tareas, name='tareas'),
    path('tareasFinalizadas/', views.tareasFinalizadas, name='tareasFinalizadas'),
    path('logout/', views.cerrarSesion, name='logout'),
    path('iniciarSesion/', views.iniciarSesion, name='iniciarSesion'),
    path('crear_tarea/', views.crearTarea, name='crearTarea'),
    path('eliminarTarea/<int:idTarea>', views.eliminarTarea, name='eliminarTarea'),
    path('detalle_tarea/<int:idTarea>/', views.detalleTarea, name='detalle_tarea'),
    path('detalle_tarea/<int:idTarea>/completarTarea', views.completarTarea, name='completarTarea'),
    path('', views.inicio, name='inicio'),
    
    
]
