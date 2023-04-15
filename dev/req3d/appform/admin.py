from django.contrib import admin

# Register your models here.

from .models import Articles

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('number', 'project_name', 'time_created', 'user', 'status')
    search_fields = ('number', 'project_name')
    list_filter = ('status',)

    fieldsets = (
        ('Информация о запросе', {
            'fields': ('number', 'user', 'mail', 'name', 'op', 'course', 'project_name', 'teach_name', 'phone', 'status', 'comment', 'time_created')
        }),
        ('Приложения к заявке', {
            'fields': ('dmodel', 'note')
        }),
    )
    readonly_fields = ('number', 'user', 'mail', 'name', 'op', 'course', 'project_name', 'teach_name', 'phone', 'dmodel', 'note', 'time_created')

    ordering = ('number',)

admin.site.register(Articles, ArticlesAdmin)