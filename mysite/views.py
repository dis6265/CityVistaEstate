from django.http import HttpResponse
from django.shortcuts import render
import mysql.connector as sql

def homepage(request):
    return render(request,"index2.html")

def login(request):
    return render(request,"internalfiles/login.html")

# def registration(request):
#     return render(request,"internalfiles/Registration.html")

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

def userform(request):
    finalans=0
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
        c="insert into users Values('{}','{}','{}','{}','{}','{}')".format(fn,ln,em,pwd,mn,ct)
        cursor.execute(c)
        obj.commit()
    
    return render(request,"internalfiles/Registration.html")


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
