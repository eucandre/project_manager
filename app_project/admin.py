from django.contrib import admin
from .models import Project


class ProjetoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'start',
         'end', 'goal', 'field', 'members', 'responsable', 'cost', 'status', 'attachment')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('title', 'start', 'end')
            }
        ),
    )

    list_display = ('title', 'start', 'end', 'responsable', 'status')
    list_filter = ('start', 'end', 'title')
    search_fields = ('start', 'end', 'title')
    ordering = ('start',)


admin.site.register(Project, ProjetoAdmin)
