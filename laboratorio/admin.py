from django.contrib import admin

from .models import CategoriaQuimica, Reactivo


@admin.register(CategoriaQuimica)
class CategoriaQuimicaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ubicacion']
    list_filter = ['ubicacion'] 
    search_fields = ['nombre', 'descripcion']


@admin.register(Reactivo)
class ReactivoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'numero_cas', 'categoria', 'cantidad', 'unidad', 'fecha_vencimiento', 'es_peligroso']
    list_filter = ['categoria', 'es_peligroso', 'unidad']
    search_fields = ['nombre', 'numero_cas', 'categoria__nombre'] 
    list_select_related = ['categoria'] 