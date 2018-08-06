from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse
from .forms import ContactForm
from django.conf import settings
from  django.core.mail import send_mail
from django.template import loader
from .models import Api


# Create your views here.
""" def index(request):
    return render(request,'polls/index.html') """

#here is the same code tht loads the tempalte from the view
def index(request):
    context = locals()
    #template = loader.get_template('polls/index.html')
    template = 'polls/index.html'
    return render(request, template,context)

def Login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username = username, password = password)
    if user is not None and user.is_active:
        auth.login(request,user)
    else:
        return HttpResponse("You need to login first")


#define  contact form for the contact template
def Contact(request):
    #instantiate an object of the ContactForm class
    form = ContactForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data['name']
        message = form.cleaned_data['message']
        subject = 'Message from django admin'
        comment = '%s %s',(message, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, comment,emailFrom, emailTo, fail_silently = False)
    context = locals()
    #template = loader.get_template('polls/contact.html')
    template = 'polls/contact.html'
    return render(request, template, context)
"""
def dataView(request):
    api = Api()
    return api.objects.all().order_by('-title')[:3] """
