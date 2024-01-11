from django.contrib import admin
from .models import Notes

# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    list_display = ('branch', 'subject', 'filetype','approval_status', 'status')
    ordering = ('branch',)
    search_fields = ('subject', 'beanch')
    list_editable = ('status',)

    def approval_status(self, obj):
        approved = 'Approved' if obj.status else 'Not Approved'
        return approved

    approval_status.short_description = 'Approval Status'

admin.site.register(Notes, NoteAdmin)