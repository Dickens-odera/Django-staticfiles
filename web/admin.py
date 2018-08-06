from django.contrib import admin
from .models import Api
# Register your models here.

class ApiAdmin(admin.ModelAdmin):
    class Meta:
        model = Api
admin.site.register(Api, ApiAdmin)

