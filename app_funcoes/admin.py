from django.contrib import admin
from .models import Funcao


class FuncaoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('descricao',)}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('descricao',)
            }
        ),
    )


admin.site.register(Funcao, FuncaoAdmin)
