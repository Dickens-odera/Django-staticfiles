from django.shortcuts import render
from .forms import FeedbackForm
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
	context = locals()
	template = 'blog/index.html'
	return render(request,template, context)


def Feedback(request, **kwargs):
	template = 'blog/contact.html'
	form = FeedbackForm(request.POST or None)
	if form.is_valid():
		name = form.cleaned_data['name']
		comment = form.cleaned_data['comment']

		#send the comment as mail
		subject = 'customer Feedback'
		message = '%s %s',{comment, name}
		emailFrom = form.cleaned_data['email']
		emailTo = [settings.EMAIL_HOST_USER]

		#context = '%s %s',{'title':title,'form':form}
		context = locals()
		send_mail(subject,message,emailFrom, emailTo, fail_silently = True)
		return render(request, template, context)
		
#SAFARICOM_MPESA_API
# 		import requests
# from requests.auth import HTTPBasicAuth

# consumer_key = "OxvaJDBrH1iNuopVr5xMIAvOqMtMnU6J"
# consumer_secret = "dPrdZ1RHYBFpx6Ib"
# api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

# r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

# print (r.text)