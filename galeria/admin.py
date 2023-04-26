from django.contrib import admin
from galeria.models import Fotografia

# Register your models here.

class ListandoFotografias(admin.ModelAdmin):
    list_display = ["id", "nome" ,"legenda"]
    list_display_links = ("id", "nome" ,"legenda")
    search_fields = ["nome"]

admin.site.register(Fotografia, ListandoFotografias)
