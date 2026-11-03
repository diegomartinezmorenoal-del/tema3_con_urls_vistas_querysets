import os
import django
import random
from datetime import datetime, timedelta

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_tareas.settings')
django.setup()

from tareas.models import Usuario, Proyecto, Etiqueta, Tarea, AsignacionTarea, Comentario

print("Iniciando generación de datos...")

# Crear 30 Usuarios
usuarios = []
for i in range(1, 31):
    u = Usuario.objects.create(
        nombre=f"Usuario_{i}",
        correo_electronico=f"usuario{i}@example.com",
        contrasena="password123"
    )
    usuarios.append(u)
print("30 Usuarios creados.")

# Crear 30 Proyectos
proyectos = []
for i in range(1, 31):
    p = Proyecto.objects.create(
        nombre=f"Proyecto_{i}",
        descripcion=f"Descripción detallada para el proyecto {i}.",
        duracion_estimada=round(random.uniform(10.0, 100.0), 2),
        fecha_inicio=datetime.now().date(),
        fecha_finalizacion=(datetime.now() + timedelta(days=30)).date(),
        creador=random.choice(usuarios)
    )
    p.usuarios_asignados.set(random.sample(usuarios, random.randint(1, 5)))
    proyectos.append(p)
print("30 Proyectos creados.")

# Crear 30 Etiquetas
etiquetas = []
for i in range(1, 31):
    e = Etiqueta.objects.create(
        nombre=f"Etiqueta_{i}"
    )
    etiquetas.append(e)
print("30 Etiquetas creadas.")

# Crear 30 Tareas
estados = ['Pendiente', 'Progreso', 'Completada']
tareas = []
for i in range(1, 31):
    t = Tarea.objects.create(
        titulo=f"Tarea_{i}",
        descripcion=f"Descripción de la tarea número {i}.",
        prioridad=random.randint(1, 5),
        estado=random.choice(estados),
        completada=random.choice([True, False]),
        hora_vencimiento=datetime.now().time(),
        creador=random.choice(usuarios),
        proyecto=random.choice(proyectos)
    )
    t.etiquetas_asociadas.set(random.sample(etiquetas, random.randint(1, 3)))
    tareas.append(t)
print("30 Tareas creadas.")

# Crear 30 Asignaciones de Tareas
asignaciones = 0
while asignaciones < 30:
    u = random.choice(usuarios)
    t = random.choice(tareas)
    if not AsignacionTarea.objects.filter(usuario=u, tarea=t).exists():
        AsignacionTarea.objects.create(
            usuario=u,
            tarea=t,
            observaciones=f"Observación de asignación para {t.titulo}"
        )
        asignaciones += 1
print("30 Asignaciones de Tarea creadas.")

# Crear 30 Comentarios
for i in range(1, 31):
    Comentario.objects.create(
        contenido=f"Este es el comentario número {i}.",
        autor=random.choice(usuarios),
        tarea=random.choice(tareas)
    )
print("30 Comentarios creados.")

print("¡Poblado completado con éxito!")