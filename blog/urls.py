from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index, name='index'),
	#path('blog/',views.contact, name='Feedback')
]