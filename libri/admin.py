from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    display_lista  = ('titolo', 'autore', 'prezzo', 'disponibile')
    campi_ricerca = ('titolo', 'autore')
    filtro_lista = ('disponibile',)
# Register your models here.
