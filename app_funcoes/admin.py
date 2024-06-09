from django.contrib import admin
from .models import Function


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


admin.site.register(Function, FuncaoAdmin)
