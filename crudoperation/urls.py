"""
URL configuration for crudoperation project.

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
from django.urls import path, include
from main.views import *
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("",home,name='home'),
    path("user/", index,name='index'),
    path("user/detail/<int:id>/",detail,name='detail'),
    path('family/',family,name='family'),
    path("family/family_detail/<int:id>/",family_detail,name='family_detail'),
    path("homep/",TemplateView.as_view(template_name='home_p.html'),name="home_p"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("signup/",signUpView,name='signup'),
    path('createuser/',createUser,name='createuser'),
    path('createfamily/',createFamily,name='createfamily'),
    path('update-details/<int:id>/',update_family,name='update-details'),
    path('family/delete-details/<int:id>/',delete_family,name='delete-details'),
    path('update-user/<int:id>/',update_user,name='update-user'),
    path('delete-user/<int:id>/',delete_user,name='delete-user'),
    path('family-tree/<int:id>/',tree,name='family-tree'),
    
]
