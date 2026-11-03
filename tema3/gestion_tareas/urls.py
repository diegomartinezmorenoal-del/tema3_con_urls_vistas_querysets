from django.contrib import admin
from django.urls import path
from tareas import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.inicio, name="inicio"),
    path("proyectos/", views.proyectos, name="proyectos"),
    path("proyecto/<int:proyecto_id>/tareas/", views.tareas_proyecto, name="tareas_proyecto"),
    path("tarea/<int:tarea_id>/usuarios/", views.usuarios_tarea, name="usuarios_tarea"),
    path("asignaciones/observaciones/<str:texto>/", views.tareas_por_observacion, name="tareas_por_observacion"),
    path("tareas/completadas/<int:anio_inicio>/<int:anio_fin>/", views.tareas_completadas_entre, name="tareas_completadas_entre"),
    path("proyecto/<int:proyecto_id>/ultimo-comentario/", views.ultimo_comentario_proyecto, name="ultimo_comentario"),
    path("tarea/<int:tarea_id>/comentarios/<str:palabra>/<int:anio>/", views.comentarios_filtrados, name="comentarios_filtrados"),
    path("proyecto/<int:proyecto_id>/etiquetas/", views.etiquetas_proyecto, name="etiquetas_proyecto"),
    path("usuarios/sin-asignar/", views.usuarios_sin_asignar, name="usuarios_sin_asignar"),
]

handler400 = "tareas.views.error400"
handler403 = "tareas.views.error403"
handler404 = "tareas.views.error404"
handler500 = "tareas.views.error500"
