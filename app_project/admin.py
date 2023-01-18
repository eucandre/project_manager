from django.contrib import admin
from .models import Projeto


class ProjetoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'inicio',
         'fim', 'objetivo', 'area', 'integrantes', 'responsavel', 'custo')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('titulo', 'inicio', 'fim')
            }
        ),
    )

    list_display = ('titulo', 'inicio', 'fim', 'responsavel')
    list_filter = ('inicio', 'fim', 'titulo')
    search_fields = ('inicio', 'fim', 'titulo')
    ordering = ('inicio',)


admin.site.register(Projeto, ProjetoAdmin)
