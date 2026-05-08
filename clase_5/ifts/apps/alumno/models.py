from django.db import models


class AlumnosActivosManager(models.Manager):
    def get_queryset(self):
        alumno = super().get_queryset().filter(active=True)
        return alumno


class Alumno(models.Model):
    nombre = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now=True)

    objects = AlumnosActivosManager()
    objects_all = models.Manager()
