# -*- coding: utf-8 -*-
from manager.models import Employee, Department
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField(source='department_id')
    class Meta:
        model = Employee
        fields = ('employee_id', 'name',
                  'email', 'department')
