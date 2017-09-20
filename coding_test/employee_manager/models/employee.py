# -*- coding: utf-8
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from department import Department


class Employee(models.Model):
    department = models.ForeignKey(Department.__name__,
                                   models.DO_NOTHING,
                                   blank=True,
                                   on_delete=models.CASCADE)
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=70,
                              blank=True,
                              null= True,
                              unique= True)
    created = models.DateTimeField(auto_now_add=True,
                                   blank=True)

    def __str__(self):
        return unicode(self.name).encode('utf-8', 'ignore')

    class Meta:
        verbose_name_plural = 'employees'
        managed = False
        db_table = 'employee'
