from django.contrib import admin
from service.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_icon','service_title','service_des','service_img','service_img1','service_img2','service_img3','service_img4')


admin.site.register(Service,ServiceAdmin)
# Register your models here.

