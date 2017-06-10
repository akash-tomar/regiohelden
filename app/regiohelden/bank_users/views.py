from django.shortcuts import render
from django.http import HttpResponseRedirect

def login(request):
	return render(request,'login.html',{})

def logout(request):
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