from django.contrib import admin

from company.models import Department, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """ Админка департаментов """
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """ Админка сотрудников """
    pass
