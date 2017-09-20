from django.shortcuts import render
from manager.models import Employee
from django.http import Http404
from api.serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EmployeeList(APIView):
    """List all employee."""
    def get(self, request, format=None):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

class EmployeeId(APIView):
    """List specific employee by id."""
    def get(self, request, pk, format=None):
        employee = Employee.objects.get(employee_id=pk)
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)
