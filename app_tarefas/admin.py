from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'start',
         'end', 'goal', 'responsable', 'id_marco', 'cost', 'status', 'attachment')}),
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

    list_display = ('title', 'id_marco', 'start', 'end', 'responsable')
    list_filter = ('start', 'end', 'title')
    search_fields = ('start', 'end', 'title')
    ordering = ('start',)


admin.site.register(Task, TaskAdmin)
