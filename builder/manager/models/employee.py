# -*- coding: utf-8
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from .department import Department


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=70,
                              blank=True,
                              null= True,
                              unique= True)
    created = models.DateTimeField(auto_now_add=True,
                                   blank=True)
    department = models.ForeignKey('Department',
                                   default=None,
                                   on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'manager'
        verbose_name_plural = 'employees'
        db_table = 'employee'
