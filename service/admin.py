from django.contrib import admin
from service.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_name','service_img','service_img1','service_img2','service_img3','service_type','service_avail','service_creation_data','service_update_data','service_address','latitude','longitude','service_des') 

    # 'service_creation_data','service_update_data'


admin.site.register(Service,ServiceAdmin)
# Register your models here.

