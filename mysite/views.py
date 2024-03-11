from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,"index2.html")

def login(request):
    return render(request,"internalfiles/login.html")

def registration(request):
    return render(request,"internalfiles/Registration.html")

def service(request):
    return render(request,"internalfiles/services.html")

def aboutUs(request):
    # return HttpResponse("welcome to mysite")
    return render(request,"internalfiles/about-us.html")



# def course(request):
#     return HttpResponse("<b> welcome to mysite <b>")

# def courseDetails(request,id):
#     return HttpResponse(id)

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
