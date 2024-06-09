from django.contrib import admin
from .models import Field


class FieldAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('description',)}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('description',)
            }
        ),
    )


admin.site.register(Field, FieldAdmin)
