from django.contrib import admin
from .models import Tarefa


class TarefaAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'inicio',
         'fim', 'objetivo', 'responsavel', 'id_marco', 'custo', 'status', 'attachment')}),
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

    list_display = ('titulo', 'id_marco', 'inicio', 'fim', 'responsavel')
    list_filter = ('inicio', 'fim', 'titulo')
    search_fields = ('inicio', 'fim', 'titulo')
    ordering = ('inicio',)


admin.site.register(Tarefa, TarefaAdmin)
