# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True,
                                   blank=True)


    class Meta:
        app_label = 'manager'
        verbose_name_plural = 'departments'
        db_table = 'department'

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.name
