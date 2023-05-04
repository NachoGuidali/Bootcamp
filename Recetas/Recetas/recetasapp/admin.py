from django.contrib import admin
from .models import Receta, Ingrediente, Paso



class PasoInline(admin.TabularInline):
    model = Paso
    extra=0

class IngredienteInline(admin.TabularInline):
    model = Ingrediente
    extra = 0

class RecetaAdmin(admin.ModelAdmin):
    inlines = [IngredienteInline, PasoInline]
    list_display = ["nombre", "created_at"]
    prepopulated_fields = {"slug" : ("nombre", "usuario")}

admin.site.register(Receta, RecetaAdmin)