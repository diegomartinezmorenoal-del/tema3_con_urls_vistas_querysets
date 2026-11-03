from django.db import models

# 1. Usuario
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


# 2. Proyecto
class Proyecto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    duracion_estimada = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    
    # Creador
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='proyectos_creados')
    # Proyectos Asignados
    usuarios_asignados = models.ManyToManyField(Usuario, related_name='proyectos_asignados')

    def __str__(self):
        return self.nombre


# 3. Etiqueta
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


# 4. Tarea
class Tarea(models.Model):
    OPCIONES_ESTADO = [
        ('Pendiente', 'Pendiente'),
        ('Progreso', 'Progreso'),
        ('Completada', 'Completada'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    prioridad = models.IntegerField()
    estado = models.CharField(max_length=20, choices=OPCIONES_ESTADO, default='Pendiente')
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateField(auto_now_add=True)
    hora_vencimiento = models.TimeField()
    
    # Relaciones
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tareas_creadas')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')
    etiquetas_asociadas = models.ManyToManyField(Etiqueta, related_name='tareas')
    usuarios_asignados = models.ManyToManyField(Usuario, through='AsignacionTarea', related_name='tareas_asignadas')

    def __str__(self):
        return self.titulo


# 5. Asignación de Tarea (Tabla intermedia)
class AsignacionTarea(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True, null=True)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'tarea')


# 6. Comentario
class Comentario(models.Model):
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)
    
    # Relaciones
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentarios')
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='comentarios')

    def __str__(self):
        return f"Comentario de {self.autor.nombre}"