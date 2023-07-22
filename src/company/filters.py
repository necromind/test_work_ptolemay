from django_filters import FilterSet, CharFilter, NumberFilter

from company.models import Employee


class EmployeeFilter(FilterSet):
    fio = CharFilter(lookup_expr='icontains')
    department_id = NumberFilter(lookup_expr='exact')

    class Meta:
        model = Employee
        fields = ['fio', 'department_id']
