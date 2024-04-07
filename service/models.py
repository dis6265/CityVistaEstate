from django.db import models
# from django.contrib.gis.db import models

# Create your models here.
class Service(models.Model):
    # service_name= models.CharField(max_length=50)
    # # service_add = models.PointField()
    # service_img = models.FileField(upload_to="service/",max_length=250, null=True,default=None)
    # service_img1 = models.FileField(upload_to="service/",max_length=250, null=True,default=None)
    # service_img2 = models.FileField(upload_to="service/",max_length=250, null=True,default=None)
    # service_img3 = models.FileField(upload_to="service/",max_length=250, null=True,default=None)
    # service_des = models.TextField(max_length=50)
    # # service_creation_data = models.DateField(auto_now_add=True)
    # # service_update_data = models.DateField(auto_now=True)


    # service_add = models.PointField()
    service_name= models.CharField(max_length=50)
    service_img = models.FileField(upload_to="service/",max_length=250, null=True,default=None)
    service_img1 = models.FileField(upload_to="service/",max_length=250, null=True,default=None)
    service_img2 = models.FileField(upload_to="service/",max_length=250, null=True,default=None)
    service_img3 = models.FileField(upload_to="service/",max_length=250, null=True,default=None)
    service_type = models.TextField(max_length=15)
    service_avail = models.CharField(max_length=15)
    service_des = models.TextField(max_length=50)
    