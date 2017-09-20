# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True,
                                   blank=True)

    def __str__(self):
        return unicode(self.name).encode('utf-8', 'ignore')

    class Meta:
        verbose_name_plural = 'departments'
        managed = False
        db_table = 'department'
