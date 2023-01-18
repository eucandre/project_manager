from django.contrib import admin
from .models import Marco


class MarcoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('titulo', 'inicio',
         'fim', 'objetivo', 'integrantes', 'responsavel')}),
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


admin.site.register(Marco, MarcoAdmin)
