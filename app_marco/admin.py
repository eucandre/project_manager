from django.contrib import admin
from .models import FollowUp


class FollowUpAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'start', 'id_projet',
         'end', 'goal', 'members', 'responsable', 'cost', 'status')}),
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

    list_display = ('title', 'id_projet', 'start',
                    'end', 'responsable', 'status')
    list_filter = ('start', 'end', 'title')
    search_fields = ('start', 'end', 'title')
    ordering = ('start',)


admin.site.register(FollowUp, FollowUpAdmin)
