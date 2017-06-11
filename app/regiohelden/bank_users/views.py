from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.core.urlresolvers import reverse
from bank_users.forms import *
from django.contrib.auth.models import User
def login(request):
	if request.user.is_anonymous():
		return render(request,'login.html',{})
	else:
		return HttpResponseRedirect(reverse('bank_users:home'))

def logout(request):
	logout_user(request)
	return HttpResponseRedirect(reverse('bank_users:login'))

def home(request):
	if request.user.is_anonymous():
		return HttpResponseRedirect(reverse('bank_users:login'))
	created = False
	# import pdb; pdb.set_trace()
	if 'create' in request.GET:
		created = request.GET.get('create')
		if created=="1":
			created=True
		elif created=="0":
			created=False
	return render(request,'home.html',{'created':created})

def createBankingUser(request):
	if request.method=='GET':
		created = True
		if 'create' in request.GET:
			created = request.GET.get('create')
			if created=="1":
				created=True
			elif created=="0":
				created=False
		ibanform = IBANForm()
		userform = UserForm()
		return render(request,'createUser.html',{'iban':ibanform,'userform':userform,'created':created})

	elif request.method=='POST':
		ibanform = IBANForm(request.POST)
		userform = UserForm(request.POST)

		# check whether it's valid:
		if userform.is_valid() and ibanform.is_valid():
			first_name = userform.cleaned_data.get('first_name')
			last_name = userform.cleaned_data.get('last_name')

			countrycode = ibanform.cleaned_data.get('countrycode')
			checksum = ibanform.cleaned_data.get('checksum')
			swiftcode = ibanform.cleaned_data.get('swiftcode')
			accountnumber = ibanform.cleaned_data.get('accountnumber')

			user = CustomUser(first_name=first_name,last_name=last_name)
			user.save()

			iban = IBANDetail(countrycode=countrycode,checksum=checksum,swiftcode=swiftcode,accountnumber=accountnumber)
			iban.save()

			creator = User.objects.get(pk=request.user.id)
			bankuser = BankUser(user=user,iban=iban,creator=creator)
			bankuser.save()

			return HttpResponseRedirect(reverse('bank_users:home')+'?create=1')
		else:
			return HttpResponseRedirect(reverse('bank_users:add')+'?create=0')


def readBankingUser(request):
	return render(request,'readUser.html',{})

def updateBankingUser(request):
	return render(request,'updateUser.html',{})

def deleteBankingUser(request):
	return render(request,'deleteUser.html',{})