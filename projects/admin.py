from django.contrib import admin
from django.db.models import Model

from projects.models import Project
from projects.models.task import Task
from projects.models.projects import Project
from projects.models.tag import Tag
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'status', 'priority', 'created_at', 'due_date')
    search_fields = ('name',)
    list_filter = ('status', 'priority','assignee')



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    actions = ['replace_spaces']


    @admin.action(description="Replace_spaces ")
    def replace_spaces(self,request,query_set):
        for project in query_set:
            project.name = project.name.strip().replace(' ','_')
            project.save()






@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
