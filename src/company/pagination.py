from django.conf import settings

from rest_framework.pagination import PageNumberPagination


class EmployeePagination(PageNumberPagination):
    page_size = settings.EMPLOYEE_API_PAGE_SIZE
