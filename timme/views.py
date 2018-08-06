from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template , Context
#from django.forms.models import *

# Create your views here.
#callculate the current date
""" def current_time(request):
    now = datetime.now()
    html = "<html><head></head><body> The time is %s.</body>></html>" % now
    return HttpResponse(html)
 """
# here is the same code using django template system
#inorder to use the template system we have to first import the Template and Context from the django.template library
def current_time(request):
     now = datetime.now()
     t = Template('<html><body>The time is {{current_time}}</body></html>')
     html = t.render(Context({'current_time':now}))
     return HttpResponse(html)

""" 
def ContactForm(forms.Form):
    choice = forms.ChoiceField()
    message = forms.CharField() """
