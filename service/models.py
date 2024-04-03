from django.db import models

# Create your models here.
class Service(models.Model):
    service_icon = models.CharField(max_length=50)
    service_title = models.CharField(max_length=50)
    service_des = models.TextField(max_length=50)
    service_img = models.FileField(upload_to="service/",max_length=250, null=True,default=None)
    service_img1 = models.FileField(upload_to="service/",max_length=250, null=True,default=None)
    service_img2 = models.FileField(upload_to="service/",max_length=250, null=True,default=None)
    service_img3 = models.FileField(upload_to="service/",max_length=250, null=True,default=None)
    service_img4 = models.FileField(upload_to="service/",max_length=250, null=True,default=None)

# class Image(models.Model):
#     image = models.ImageField(upload_to='images/')
#     description = models.TextField()