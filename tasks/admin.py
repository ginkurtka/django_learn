from django.contrib import admin
from .models import Project, Tasks

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    pass
