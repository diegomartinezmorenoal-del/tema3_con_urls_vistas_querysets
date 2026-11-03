from django.contrib import admin
from .models import Usuario, Proyecto, Etiqueta, Tarea, AsignacionTarea, Comentario

admin.site.register(Usuario)
admin.site.register(Proyecto)
admin.site.register(Etiqueta)
admin.site.register(Tarea)
admin.site.register(AsignacionTarea)
admin.site.register(Comentario)
