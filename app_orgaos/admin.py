from django.contrib import admin
from .models import Orgao


class OrgaoAdmin(admin.ModelAdmin):
    list_display = ('name', 'acronym', 'chef', 'address',
                    'phone', 'email', 'website', 'active')
    list_filter = ('name', 'acronym')
    search_fields = ('name', 'acronym')
    ordering = ('name',)
    list_per_page = 25


admin.site.register(Orgao, OrgaoAdmin)
