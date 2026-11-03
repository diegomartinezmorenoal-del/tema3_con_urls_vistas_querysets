from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Usuario, Proyecto, Tarea, AsignacionTarea, Comentario, Etiqueta

def inicio(request):
    return render(request, "tareas/inicio.html")

def proyectos(request):
    datos = Proyecto.objects.select_related("creador").prefetch_related("usuarios_asignados").all().order_by("id")
    return render(request, "tareas/lista.html", {"titulo":"Todos los proyectos", "objetos":datos, "tipo":"proyectos"})

def tareas_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    datos = Tarea.objects.filter(proyecto=proyecto).select_related("creador").order_by("-fecha_creacion", "-id")
    return render(request, "tareas/lista.html", {"titulo":f"Tareas del proyecto: {proyecto.nombre}", "objetos":datos, "tipo":"tareas"})

def usuarios_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    datos = AsignacionTarea.objects.filter(tarea=tarea).select_related("usuario").order_by("fecha_asignacion")
    return render(request, "tareas/lista.html", {"titulo":f"Usuarios asignados a: {tarea.titulo}", "objetos":datos, "tipo":"asignaciones"})

def tareas_por_observacion(request, texto):
    datos = AsignacionTarea.objects.filter(observaciones__icontains=texto).select_related("usuario","tarea").order_by("tarea__titulo")
    return render(request, "tareas/lista.html", {"titulo":f'Asignaciones con observaciones que contienen "{texto}"', "objetos":datos, "tipo":"asignaciones_texto"})

def tareas_completadas_entre(request, anio_inicio, anio_fin):
    if anio_inicio > anio_fin:
        anio_inicio, anio_fin = anio_fin, anio_inicio
    datos = Tarea.objects.filter(estado="Completada", fecha_creacion__year__gte=anio_inicio, fecha_creacion__year__lte=anio_fin).order_by("-fecha_creacion")
    return render(request, "tareas/lista.html", {"titulo":f"Tareas completadas entre {anio_inicio} y {anio_fin}", "objetos":datos, "tipo":"tareas"})

def ultimo_comentario_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    comentario = Comentario.objects.filter(tarea__proyecto=proyecto).select_related("autor","tarea").order_by("-fecha_comentario","-id").first()
    return render(request, "tareas/ultimo_comentario.html", {"proyecto":proyecto, "comentario":comentario})

def comentarios_filtrados(request, tarea_id, palabra, anio):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    datos = Comentario.objects.filter(tarea=tarea, contenido__istartswith=palabra, fecha_comentario__year=anio).select_related("autor").order_by("fecha_comentario")
    return render(request, "tareas/lista.html", {"titulo":f'Comentarios de "{tarea.titulo}" que empiezan por {palabra} ({anio})', "objetos":datos, "tipo":"comentarios"})

def etiquetas_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    datos = Etiqueta.objects.filter(tareas__proyecto=proyecto).distinct().order_by("nombre")
    return render(request, "tareas/lista.html", {"titulo":f"Etiquetas usadas en {proyecto.nombre}", "objetos":datos, "tipo":"etiquetas"})

def usuarios_sin_asignar(request):
    datos = Usuario.objects.exclude(tareas_asignadas__isnull=False).distinct().order_by("nombre")
    return render(request, "tareas/lista.html", {"titulo":"Usuarios que no están asignados a ninguna tarea", "objetos":datos, "tipo":"usuarios"})

def error400(request, exception):
    return render(request, "tareas/error.html", {"codigo":400,"mensaje":"La petición no es válida."}, status=400)
def error403(request, exception):
    return render(request, "tareas/error.html", {"codigo":403,"mensaje":"No tienes permiso para acceder a esta página."}, status=403)
def error404(request, exception):
    return render(request, "tareas/error.html", {"codigo":404,"mensaje":"No se ha encontrado la página solicitada."}, status=404)
def error500(request):
    return render(request, "tareas/error.html", {"codigo":500,"mensaje":"Ha ocurrido un error interno del servidor."}, status=500)
