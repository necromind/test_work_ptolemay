from rest_framework import serializers

from company.models import Employee, Department


class DepartmentSerializer(serializers.ModelSerializer):
    employees_count = serializers.IntegerField(min_value=0)
    salary_total = serializers.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        model = Department
        fields = [
            'id',
            'title',
            'employees_count',
            'salary_total',
        ]


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'id',
            'fio',
            'photo',
            'position',
            'salary',
            'age',
            'department',
        ]
