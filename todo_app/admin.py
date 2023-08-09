from django.contrib import admin
from . models import Todo
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task','is_completed','updated_at')


admin.site.register(Todo,TaskAdmin)