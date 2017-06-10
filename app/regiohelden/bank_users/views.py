from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.core.urlresolvers import reverse


def login(request):
	if request.user.is_anonymous():
		return render(request,'login.html',{})
	else:
		return HttpResponseRedirect(reverse('bank_users:home'))

def logout(request):
	logout_user(request)
	return HttpResponseRedirect(reverse('bank_users:login'))

def home(request):
	return render(request,'home.html',{})

def createBankingUser(request):
	return render(request,'createUser.html',{})

def readBankingUser(request):
	return render(request,'readUser.html',{})

def updateBankingUser(request):
	return render(request,'updateUser.html',{})

def deleteBankingUser(request):
	return render(request,'deleteUser.html',{})