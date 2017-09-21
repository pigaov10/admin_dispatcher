# -*- coding: utf-8 -*-
from manager.models import Employee, Department
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('department_id', 'name',)


class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)

    department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(),
                                                       source='department',
                                                       write_only=True)

    class Meta:
        model = Employee
        fields = ('department_id', 'name',
                  'department', 'email', 'employee_id',)
