from django.http import HttpResponse
from django.shortcuts import render, redirect
import mysql.connector as sql
from django.db import IntegrityError

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
            if key=="City":
                ct=value

        try:
            c="insert into users Values('{}','{}','{}','{}','{}','{}')".format(fn,ln,em,pwd,mn,ct)
            cursor.execute(c)
            obj.commit()
        except :
            return render(request, 'internalfiles/Registration.html',{'form':d,'error_massage':'This email is already registered. please login'})

        # try:
        #     c="insert into users Values('{}','{}','{}','{}','{}','{}')".format(fn,ln,em,pwd,mn,ct)
        #     cursor.execute(c)
        #     obj.commit()

        # except:
            
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



    