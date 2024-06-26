from django.http import HttpResponse
from django.shortcuts import render, redirect
import mysql.connector as sql
from django.db import IntegrityError
from service.models import Service
import re
import googlemaps

from django.views.decorators.cache import never_cache

@never_cache

def homepage(request):
    
    return render(request,"index2.html")

''' def login(request):
#     return render(request,"internalfiles/login.html")

# def registration(request):
#     return render(request,"internalfiles/Registration.html")'''

def service(request):
    return render(request,"internalfiles/services.html")

def aboutUs(request):
    # return HttpResponse("welcome to mysite")
    return render(request,"internalfiles/about-us.html")

def iss(request):
    # return redirect('is')
    return render(request,"internalfiles/is.html")

def rooms(request):
    return render(request,"internalfiles/rooms.html")


def Villas(request):
    return render(request,"internalfiles/Villas.html")

def Building(request):
    return render(request,"internalfiles/Building.html")

def House(request):
    return render(request,"internalfiles/House.html")

def listyourproprty(request):
    return render(request,"internalfiles/lyp.html" )

def takeonrent(request):
    servicesData=Service.objects.all()
    data={
        'servicesData':servicesData   
    }   
    return render(request,"internalfiles/tor.html", data)


def upload_image(request):
    if request.method == 'POST': 
        try:
            Oname = request.POST['Oname']
            image = request.FILES['image']
            image1 = request.FILES.get('image1')
            image2 = request.FILES.get('image2')
            image3 = request.FILES.get('image3')
            service_type = request.POST.get('type')
            description = request.POST['description']
            address = request.POST.get('address')
            latitude = request.POST.get('latitude')  # Assuming latitude and longitude are being submitted in the form
            longitude = request.POST.get('longitude')

            # main_area = address.split(',')[0].strip()
            
            Service.objects.create(
                service_name=Oname,
                service_img=image,
                service_img1=image1,
                service_img2=image2,
                service_img3=image3,
                service_type=service_type,
                service_des=description,
                service_address=address,
                # service_ad=main_area,
                latitude=latitude,
                longitude=longitude)
            return redirect('display_images')
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}")

    # return render(request, 'internalfiles/tor.html')
    return render(request, 'internalfiles/tor.html')

def display_images(request):
    images = Service.objects.all()
    return redirect('tor')
    return render(request, 'internalfiles/tor.html', {'images': images})


fn=''
ln=''
em=''
pwd=''
mn=''
ct=''
lem=''
lpwd=''
def userform(request):    
    global fn,ln,em,pwd,mn,ct
    if request.method=='POST':
        obj=sql.connect(host="localhost",user="root",password="dishapatil",database="mysite")
        cursor=obj.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="FN":
                fn=value
            if key=="LN":
                ln=value
            if key=="mail":
                em=value
            if key=="pass":
                pwd=value
            if key=="MN":
                mn=value
                if not re.match(r'^[6-9]\d{9}$', value):
                    return render(request, 'internalfiles/Registration.html', {'form': d, 'Mobile_number_error_message': 'Invalid mobile number.'})
                
            if key=="City":
                ct=value

        try:
            c="insert into users Values('{}','{}','{}','{}','{}','{}')".format(fn,ln,em,pwd,mn,ct)
            cursor.execute(c)
            obj.commit()
        except :
            return render(request, 'internalfiles/Registration.html',{'form':d,'error_massage':'This email is already registered. please login'})

            
        return redirect('login')
    return render(request,"internalfiles/Registration.html")


def loginform(request):
    global lem,lpwd
    if request.method=='POST':        
        obj=sql.connect(host="localhost",user="root",password="dishapatil",database="mysite")
        cursor=obj.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="UserName":
                lem=value
            if key=="Password":
                lpwd=value
        c="select * from users where email='{}' and password='{}'".format(lem, lpwd)    
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        #t=(cursor.fetchall()) 
        print("Empty {}".format(t))
        if t==():
             print("Empty {}".format(t))
             return render(request, 'internalfiles/login.html',{'form':d,'error_massage':'invalid email or password. Please re-enter'})
    
        else:
            print("Empty {}".format(t))
            return redirect('service')
            # return render(request,"internalfiles/services.html")
    return render(request,"internalfiles/login.html",{'output':em})

'''def homepage(request):
    data={
        "title":"Home Page",
        "bdata" : "welcome to mysiye",
        "clist" :['C','C++','Python'],
        "list" :[],#10,20,30,40,5,15
        'sd':[
            {'name':'disha','phone':9876543321},
            {'name':'patil','phone':9827318283}
        ]
    }
    
    return render(request,"index2.html",data)'''



    