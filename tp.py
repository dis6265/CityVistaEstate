'''#Program for obtaining Col Names of table
#OracleColNamesEx2.py
import cx_Oracle
def getcolnames():
    try:
        con = cx_Oracle.connect("system/manager@localhost/xe")
        cur = con.cursor()
        cur.execute("select * from employee")
        #Code for getting Col names
        print("============================")
        for colname in [metadata[0] for  metadata in cur.description]:
            print(colname,end="\t")
        print()
        print("============================")
        #Code for getting Records
        records=cur.fetchall()
        for record in records:
            for val in record:
                print("{}".format(val),end="\t")
            print()
        print("============================")
    except cx_Oracle.DatabaseError as db:
        print("Problem Oracle DB:",db)

#main program
getcolnames()'''


from django.http import HttpResponse
from django.shortcuts import render
import mysql.connector as sql

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
        c="insert into users Values('{}','{}','{}','{}','{}','{}')".format(fn,ln,em,pwd,mn,ct)
        cursor.execute(c)
        obj.commit()
    
    return render(request,"internalfiles/Registration.html")


def loginform(request):
    global lem,lpwd
    if request.method=='POST':        
        obj=sql.connect(host="localhost",user="root",password="dishapatil",database="mysite")
        cursor=obj.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="mail":
                lem=value
            if key=="pass":
                lpwd=value
        c="select * from users where email='{}' and password='{}'".format(lem, lpwd)    
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        #t=(cursor.fetchall()) 
        print("Empty {}".format(t))
        if t==():
             print("Empty {}".format(t))

             return render(request, 'internalfiles/login.html',{'form':d,'error_massage':'invalid email or password. Please re-enter'})
            # return render(request,"internalfiles/services.html")
        else:
            print("Empty {}".format(t))
            return render(request, 'welcome.html')
            #return render(request,"internalfiles/services.html")
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





'''# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STATICFILES_DIRS=[
    BASE_DIR,"static"
]'''
