from django.contrib import admin
from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'telefone', 'email', 'descricao', 'listado')
    list_display_links = ('nome', 'sobrenome')
    list_filter = ('nome', 'sobrenome', 'categoria')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome')
    list_editable = ('telefone', 'email', 'listado')


admin.site.register(Contato, ContatoAdmin)
admin.site.register(Categoria)
