"""django_social_auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from bank_users.views import *
from django.conf.urls import include


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^add/',createBankingUser,name='addUser'),
    url(r'^delete/',deleteBankingUser,name='deleteUser'),
    url(r'^update/',updateBankingUser,name='updateUser'),
    url(r'^view/',readBankingUser,name='viewUser'),
    url(r'^login/',login,name='login'),
    url(r'^logout/',logout,name='logout'),
]