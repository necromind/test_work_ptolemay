from django.core.validators import MinValueValidator
from django.db import models


class Department(models.Model):
    """ Модель департамента. """
    title = models.CharField('Название', max_length=30, unique=True)

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'

    def __str__(self):
        return self.title


class Employee(models.Model):
    """ Модель сотрудника. """
    fio = models.CharField('Имя', max_length=100, db_index=True)
    photo = models.FileField('Фото', upload_to='photos', blank=True, null=True)
    position = models.CharField('Должность', max_length=100)
    salary = models.DecimalField(
        'Оклад',
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.0)]
    )
    age = models.PositiveIntegerField(
        'Возраст',
        validators=[MinValueValidator(0)]
    )
    department = models.ForeignKey(
        Department,
        verbose_name='Департамент',
        on_delete=models.CASCADE,
        related_name='employees'
    )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        unique_together = ('id', 'department')

    def __str__(self):
        return self.fio
