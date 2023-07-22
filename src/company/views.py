from django.db.models import Count, Sum

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from company.filters import EmployeeFilter
from company.models import Employee, Department
from company.pagination import EmployeePagination
from company.serializers import DepartmentSerializer, EmployeeSerializer


class DepartmentListAPIView(generics.ListAPIView):
    """ Список департаментов. """
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        queryset = Department.objects.prefetch_related('employees').annotate(
            employees_count=Count('employees'),
            salary_total=Sum('employees__salary')
        )
        return queryset


class EmployeeViewSet(ModelViewSet):
    """ CRUD сотрудников. """
    queryset = Employee.objects.select_related('department')
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeSerializer
    filterset_class = EmployeeFilter
    pagination_class = EmployeePagination
    ordering = ('id')
