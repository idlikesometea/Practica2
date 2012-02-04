from django.contrib import admin
from main.models import Encuesta, Respuesta


class Respuestas(admin.StackedInline):
    model = Respuesta
    extra = 3

class RespuestasAdmin(admin.ModelAdmin):
    campos = [
        (None,    {'campos': ['pregunta']}),
        ('Fecha', {'campos': ['fecha'], 'classes': ['colapsar']})
    ]
    inlines = [Respuestas]

admin.site.register(Encuesta, RespuestasAdmin)
