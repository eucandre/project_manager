from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Area

from django.contrib import admin


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
