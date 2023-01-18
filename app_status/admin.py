from django.contrib import admin
from .models import Status


class StatusAdmin(admin.ModelAdmin):
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


admin.site.register(Status, StatusAdmin)
