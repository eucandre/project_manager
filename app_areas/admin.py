from django.contrib import admin
from .models import Area


class AreaAdmin(admin.ModelAdmin):
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


admin.site.register(Area, AreaAdmin)
