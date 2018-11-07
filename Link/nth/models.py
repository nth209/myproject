# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
# Create your models here.
class slink(models.Model):
    LinkID = models.AutoField(primary_key=True)
    LinkName = models.CharField("Tên để nhớ", max_length=2000 , blank=True, null=True)
    LinkURL= models.TextField("Link",max_length=2000,)
    LinkDate = models.DateField("Ngày luu",default=datetime.now,blank=True,null=True)
    LinkDescription = models.TextField("Lưu ý",max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.LinkURL