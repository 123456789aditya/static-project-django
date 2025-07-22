from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def register(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirmpassword=request.POST.get("confirmpassword")
        phone=request.POST.get("phone")
        user=Student.objects.filter(email=email)
        if user:
            return render(request,'register.html')
        else:
            if password==confirmpassword:
                Student.objects.create(name=name,email=email,password=password,confirmpassword=confirmpassword,phone=phone)
                return render(request,'login.html')
    else:
        return render(request,'register.html')        
    
    
    
    
def login(request):
    return render(request,'login.html')
def logindata(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        if email=="admin@gmail.com" and password=="admin":
            data1={
                "name":"admin",
                "email":"admin@gmail.com",
                "password":"admin"
            }
            return render(request,'admindashboard.html',{'data1':data1})
        else:
            user=Student.objects.filter(email=email)
            if user:
                userdata=Student.objects.get(email=email)
                data={'name':userdata.name,'email':userdata.email,'password':userdata.password,'confirmpassword':userdata.confirmpassword,'phone':userdata.phone}
                return render(request,'userdashboard.html',{'data':data})
    else:
        return render(request,'login.html')
                
    
def userdashboard(request):
    return render(request,'userdashboard.html')
def admindashboard(request):
    return render(request,'admindashboard.html')