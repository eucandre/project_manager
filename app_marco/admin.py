from django.contrib import admin
from .models import Marco


class MarcoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'inicio', 'id_projeto',
         'fim', 'objetivo', 'integrantes', 'responsavel', 'custo', 'status')}),
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

    list_display = ('titulo', 'id_projeto', 'inicio',
                    'fim', 'responsavel', 'status')
    list_filter = ('inicio', 'fim', 'titulo')
    search_fields = ('inicio', 'fim', 'titulo')
    ordering = ('inicio',)


admin.site.register(Marco, MarcoAdmin)
