from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login , logout, authenticate
from .forms import formularioTareas
from django.db import IntegrityError
from .models import Tarea,models
from django.utils import timezone
from django.contrib.auth.decorators import login_required
def registro(request):

    if request.method == "GET":
        return render(request, "registro.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                usuario = User.objects.create_user(
                    request.POST["username"], request.POST["password1"]
                )
                usuario.set_password(request.POST["password1"])
                usuario.save()
                auth_login(request, usuario)
                return redirect("tareas")
            except IntegrityError:
                return render(
                    request,
                    "registro.html",
                    {"form": UserCreationForm, "error": "The user exists"},
                )

        else:
            return render(
                request,
                "registro.html",
                {"form": UserCreationForm, "error": "Passwords doesn't match"},
            )


def inicio(request):

    return render(request, "inicio.html")

@login_required(login_url='iniciarSesion', redirect_field_name=None)
def tareas(request):
    print(request.POST.getlist('completadas'))
    tareas = Tarea.objects.filter(usuario=request.user, fecha_completado__isnull=True)
    if request.method == "GET":
        return render(request, "tareas.html", {'tareas' : tareas, 'btnTareas' : 'Tareas completadas'})




@login_required(login_url='iniciarSesion', redirect_field_name=None)
def tareasFinalizadas(request):
    tareas = Tarea.objects.filter(usuario=request.user, fecha_completado__isnull=False).order_by('-fecha_completado')
    if request.method == "GET":
        return render(request, "tareas.html", {'tareas' : tareas, 'btnTareas' : ' Tareas pendientes'})
   
@login_required(login_url='iniciarSesion', redirect_field_name=None)   
def detalleTarea(request, idTarea):
    if request.method == 'GET':
        tarea = get_object_or_404(Tarea,pk=idTarea,usuario=request.user)
        formularioEdicion = formularioTareas(instance=tarea)
        return render(request, "detalle_tarea.html", {'tarea' : tarea, 'form': formularioEdicion})
    else:
        try:    
            tareaEditada = get_object_or_404(Tarea, pk = idTarea,usuario=request.user)    
            formularioEditado = formularioTareas(request.POST, instance=tareaEditada)
            formularioEditado.save()
            return redirect("tareas")
        except:
            return render(request, "detalle_tarea.html", {'tarea' : tarea, 'form': formularioEdicion, "error": "Error editing tasks\n put correct values"})
@login_required(login_url='iniciarSesion', redirect_field_name=None)            
def completarTarea(request, idTarea):
    
    if request.method == 'GET':
        tarea = get_object_or_404(Tarea,pk=idTarea,usuario=request.user)
        tarea.fecha_completado = timezone.now()
        tarea.save()
        return redirect("tareas")
@login_required(login_url='iniciarSesion', redirect_field_name=None)    
def eliminarTarea(request, idTarea):
    if request.method == 'GET':
        tarea = get_object_or_404(Tarea,pk=idTarea,usuario=request.user)
        tarea.delete()
        return redirect("tareas")
         
@login_required(login_url='iniciarSesion', redirect_field_name=None)       
def crearTarea(request):
 if request.method == "GET":
   return render(
                request,
                "crear_tarea.html",
                {"form": formularioTareas}
            )
 else:
    try:  
            formularioRellenado = formularioTareas(request.POST)
            tarea = formularioRellenado.save(commit = False)
            tarea.usuario = request.user
            tarea.save()
            return redirect("tareas")
        
    except ValueError:
            return render(
            request,
                        "crear_tarea.html",
                        {"form": formularioTareas, "error": "Error creating Task\n put correct values"},
                    )

def cerrarSesion(request):

    logout(request)
    return redirect("inicio")


def iniciarSesion(request):

    
    if request.method == 'GET':
        return render(request, 'iniciarSesion.html', {'form': AuthenticationForm})
    else:
        
        usuario = request.POST['username']
        contrasenia = request.POST['password']
        
        user = authenticate(request,username = usuario,password = contrasenia)
        print(user)
        if user is None:
             return render(request, 'iniciarSesion.html',{'form': AuthenticationForm, 'error': 'Incorrect credentials'})
        else:
            auth_login(request,user)
            return redirect("tareas")
        



