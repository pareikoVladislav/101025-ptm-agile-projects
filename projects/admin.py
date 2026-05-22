from django.contrib import admin
from projects.models.task import Task
from projects.models.projects import Project
from projects.models.tag import Tag
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'status', 'priority', 'created_at', 'due_date')
    search_fields = ('name',)
    list_filter = ('status', 'priority')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
