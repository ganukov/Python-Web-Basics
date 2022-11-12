from django.contrib import admin

from Models.models_exercise.models import Employee, Department, Project


# admin.py
# This model is enabled in django admin
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name')
    list_filter = ('first_name', 'email')

    fieldsets = ('Personal Info', {'fields': ('first_name', 'last_name','age','department','email')},
                 ),


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


# @admin.register(NullBlankDemo)
# class NullBlankDemoAdmin(admin.ModelAdmin):
#     pass
