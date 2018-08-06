from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include

urlpatterns = [
    url(r'^$',include('latest.urls')),
    path('admin/', admin.site.urls),
    path('web/', include('web.urls')),
    path('timme/',include('timme.urls')),
    path('blog/', include('blog.urls')),
]
