import factory

from company.models import Employee, Department


class DepartmentFactory(factory.django.DjangoModelFactory):
    """ Фабрика модели Department. """
    title = factory.Faker('text', max_nb_chars=15)

    class Meta:
        model = Department


class EmployeeFactory(factory.django.DjangoModelFactory):
    """ Фабрика модели Employee. """

    fio = factory.Faker('name')

    position = factory.Faker('text', max_nb_chars=15)
    salary = factory.Faker('pyint', min_value=0, max_value=1000000)
    age = factory.Faker('pyint', min_value=18, max_value=100)

    # department = factory.SubFactory(DepartmentFactory)

    class Meta:
        model = Employee
