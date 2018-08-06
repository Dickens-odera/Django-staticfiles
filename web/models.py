from __future__ import unicode_literals
from django.db import models
from django.forms import forms
#from django.newforms import form_for_model
# Create your models here.
TOPIC_CHOICES = (
    ('general','general enquiery'),
    ('bug','bug report'),
    ('Suggestion','suggestion'),
)
class Api(models.Model):
    title = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    website = models.URLField(default = 'https://www.mmust.ac.ke')
    def __unicode__(self):
        return self.title
    """ def __str__(self):
        return self.title """
    class Meta:
        verbose_name_plural = 'Api'


    #def __str__(self):
     #   return self.name
