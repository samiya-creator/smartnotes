from django.contrib import admin

from .models import Notes
# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

admin.site.register(Notes, NotesAdmin)
    