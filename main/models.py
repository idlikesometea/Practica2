from django.db import models

# Create your models here.

class Encuesta(models.Model):
    pregunta = models.CharField(max_length=150)
    fecha = models.DateTimeField('Fecha de publicacion')
    
    def __unicode__(self):
       return self.pregunta

class Respuesta(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    respuesta = models.CharField(max_length=200)
    votos = models.IntegerField()

    def __unicode__(self):
       return self.respuesta
