# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from manager.models import Employee, Department


class DepartmentTestCase(TestCase):

    def test_pass_create_object_department(self):
        """Test if objs are being creating successfully"""
        create_department = Department.objects.create(name="RH")
        self.assertEqual(create_department.name, 'RH')

    def test_verbose_name_plural(self):
        self.assertEqual(Department._meta.verbose_name_plural, "departments")


class EmployeeTestCase(TestCase):

    def test_pass_create_object_employee(self):
        """Test if objs are being creating successfully"""
        create_department = Department.objects.create(name="Development")
        department = Department.objects.get(name='Development')
        employee = Employee.objects.create(name="Raphael Iarussi",
                                           email='r.iarussi@hotmail.com',
                                           department=department)
        self.assertEqual(department.name, 'Development')

    def test_verbose_name_plural(self):
        self.assertEqual(Employee._meta.verbose_name_plural, "employees")
