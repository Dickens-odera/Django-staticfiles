from django.conf.urls import url
from . import  views
from django.urls import path,include
from web import views as index_view
from web import views as Contact_view
urlpatterns = [
    url(r'^$',index_view.index, name='index'),
    url(r'^contact/$', Contact_view.Contact, name='contact'),
 ]
