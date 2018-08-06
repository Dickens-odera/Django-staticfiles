from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length = 100)
    pub_date = models.DateField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Books'