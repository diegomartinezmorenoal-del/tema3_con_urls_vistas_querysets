# Tarea: URLs, Vistas y QuerySets

## Ejecutar
1. Abre una terminal dentro de la carpeta `tema3`.
2. Activa tu entorno virtual si lo tienes: `source venv/bin/activate`
3. Ejecuta `python manage.py runserver`
4. Entra en http://127.0.0.1:8000/

## Direcciones incluidas
- `/` Inicio
- `/proyectos/` Listado de proyectos
- `/proyecto/1/tareas/` Tareas del proyecto 1, más recientes primero
- `/tarea/1/usuarios/` Usuarios asignados a tarea 1, por fecha ascendente
- `/asignaciones/observaciones/observación/` Buscar palabra en observaciones (se puede cambiar el texto)
- `/tareas/completadas/2024/2026/` Tareas completadas entre los años indicados
- `/proyecto/1/ultimo-comentario/` Usuario del comentario más reciente del proyecto
- `/tarea/1/comentarios/Este/2026/` Comentarios que empiezan por texto y año
- `/proyecto/1/etiquetas/` Etiquetas utilizadas en el proyecto
- `/usuarios/sin-asignar/` Usuarios sin tareas asignadas

Los enlaces de ejemplo usan el ID 1. Si no existe, cambia ese ID por uno que tengas en la base de datos.
Los errores 400, 403, 404 y 500 tienen una plantilla común personalizada que muestra el código y mensaje.
Para comprobar errores en desarrollo, recuerda que Django con `DEBUG=True` puede mostrar páginas técnicas en lugar de algunas páginas personalizadas. En producción, configura `DEBUG=False` y `ALLOWED_HOSTS` correctamente.
