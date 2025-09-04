"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app import views


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logindata/',views.logindata,name='logindata'),
    path('userdashboard/',views.userdashboard,name='userdashboard'),
    path('admindashboard/',views.admindashboard,name='admindashboard'),
    path('addtousercart/',views.addtousercart,name='addtousercart'),
    path('cartdata/',views.cartdata,name='cartdata'),
    path('careers/',views.careers,name='careers'),
    path('careersform/',views.careersform,name='careersform'),
    path('jobapplication/',views.jobapplication,name='jobapplication'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('update/<int:pk>/',views.update,name='update'),
    path('update/uprec/<int:pk>',views.uprec,name='uprec'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
    
    
]
