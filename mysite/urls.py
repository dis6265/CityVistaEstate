"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite import views


urlpatterns = [
    path('admin/', admin.site.urls),
#    , path('course/',views.course) ,
#    path('course/<int:id>',views.courseDetails),182
#    path('course/<int:str>',views.courseDetails),django
#    path('course/<int:slug>',views.courseDetails),#about-us-or-me//value with dash
#   path('course/<id>',views.courseDetails) #any type of value
    path('',views.homepage,name="home"),
    path('login/',views.loginform,name='login'),
    # path('Registration/',views.registration),
    path('about-us/',views.aboutUs,name="about-us"),
    path('service/',views.service,name="service"),
    path('Registration/',views.userform, name="Registration"),
    path('is/',views.iss, name="is"),
    path('service/rooms' , views.rooms, name="room"),
    path('service/Building' , views.Building, name="Building"),
    path('service/House' , views.House, name="House"),
    path('service/Villas' , views.Villas, name="Villas"),


]

