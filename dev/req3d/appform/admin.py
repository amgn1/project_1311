from django.contrib import admin

# Register your models here.

from .models import Articles

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('number', 'project_name', 'user', 'status')
    search_fields = ('number', 'project_name')
    list_filter = ('status',)

    fieldsets = (
        ('Информация о запросе', {
            'fields': ('number', 'user', 'mail', 'name', 'op', 'course', 'project_name', 'teach_name', 'phone', 'status', 'comment')
        }),
        ('Приложения к заявке', {
            'fields': ('dmodel', 'note')
        }),
    )
    readonly_fields = ('number', 'user', 'mail', 'name', 'op', 'course', 'project_name', 'teach_name', 'phone', 'dmodel', 'note')

    ordering = ('number',)

admin.site.register(Articles, ArticlesAdmin)