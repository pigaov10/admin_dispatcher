# -*- coding: utf-8 -*-
from manager.models import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    # parent = serializers.RelatedField(many=True)
    class Meta:
        model = Employee
        fields = ('employee_id', 'name',
                  'email', 'department')
