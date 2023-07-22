from django.test import TestCase
from django.urls import reverse

from company.tests.factories import EmployeeFactory, DepartmentFactory


class DepartmentsTestCase(TestCase):
    def setUp(self):
        self.departments = DepartmentFactory.create_batch(2)
        self.employees = []
        for d in self.departments:
            self.employees += EmployeeFactory.create_batch(10, department=d)

    def test_department_list(self):
        """ Тесты апи списка департаментов """
