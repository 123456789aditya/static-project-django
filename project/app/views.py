from django.shortcuts import render
from .models import Student,Add_To_Cart,CareersQuery

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
            # add1=Add_To_Cart.objects.all()
            data2=CareersQuery.objects.all()
            return render(request,'admindashboard.html',{'data1':data1,'data2':data2})
        else:
            user=Student.objects.filter(email=email)
            if user:
                userdata=Student.objects.get(email=email)
                data={'name':userdata.name,'email':userdata.email,'password':userdata.password,'confirmpassword':userdata.confirmpassword,'phone':userdata.phone}
                add1=Add_To_Cart.objects.all()
                return render(request,'userdashboard.html',{'data':data,'add1':add1})
            else:
                return render(request,'login.html')
    else:
        return render(request,'login.html')
                
    
def userdashboard(request):
    return render(request,'userdashboard.html')

def admindashboard(request):
    
    return render(request,'admindashboard.html')

def addtousercart(request):
    name=request.GET.get("name")
    email=request.GET.get("email")
    password=request.GET.get("password")
    data1={
        'name':name,
        'email':email,
        'password':password
    }
    data2=CareersQuery.objects.all()
    return render(request,'admindashboard.html',{'add':data1,'data2':data2})

def cartdata(request):
    if request.method=="POST":
        image=request.FILES.get("image")
        product_name=request.POST.get("product_name")
        product_price=request.POST.get("product_price")
        # product_quantity=request.POST.get("product_quantity")
        Add_To_Cart.objects.create(image=image,product_name=product_name,product_price=product_price)
        return render(request,'admindashboard.html')
    else:
        return render(request,'admindashboard.html')
        
def careers(request):
    return render(request,'careers.html')

def careersform(request):
    return render(request,'careersform.html')

def jobapplication(request):
    if request.method=="POST":
        your_name=request.POST.get("your_name")
        email_address=request.POST.get("email_address")
        age=request.POST.get("age")
        job_description=request.POST.get("job_description")
        CareersQuery.objects.create(your_name=your_name,email_address=email_address,age=age,job_description=job_description)
        # data2=CareersQuery.objects.all()
        # return render(request,'admindashboard.html',{"data2":data2})
        return render(request,'userdashboard.html')
    else:
        return render(request,"careersform.html")
    
def delete(request,pk):
    userdata=CareersQuery.objects.get(id=pk)
    userdata.delete()
    data2=CareersQuery.objects.all()
    return render(request,'admindashboard.html',{"data2":data2})
    

# def update(request,pk):
#     old_data = CareersQuery.objects.get(id=pk)
#     data3 = {
#         'name':old_data.your_name,
#         'id':pk,
#         'email':old_data.email_address,
#         'age':old_data.age,
#         'jd':old_data.job_description
        
#     }
                
#     return render(request,'careersform.html',{'data3':data3})

def update(request,pk):
    userdata=CareersQuery.objects.get(id=pk)
    if request.method=="POST":
        return render(request,'update.html',{'userdata':userdata})
    else:
        return render(request,'update.html',{'userdata':userdata})
    
def uprec(request,pk):
    x=request.POST['your_name']
    y=request.POST['email_address']
    z=request.POST['age']
    v=request.POST['job_description']
    userdata=CareersQuery.objects.get(id=pk)
    userdata.your_name=x
    userdata.email_address=y
    userdata.age=z
    userdata.job_description=v
    userdata.save()
    data2=CareersQuery.objects.all()
    return render(request,'admindashboard.html',{'data2':data2})
    
    
    
