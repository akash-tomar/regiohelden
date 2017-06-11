from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.core.urlresolvers import reverse
from bank_users.forms import *
from django.contrib.auth.models import User
from django.http import JsonResponse
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

			user = None
			import pdb;pdb.set_trace()
			try:
				user = CustomUser(first_name=first_name,last_name=last_name)
				user.save()
			except:
				return HttpResponseRedirect(reverse('bank_users:addUser')+'?create=0')

			iban = IBANDetail(countrycode=countrycode,checksum=checksum,swiftcode=swiftcode,accountnumber=accountnumber)
			iban.save()
			creator = User.objects.get(pk=request.user.id)
			bankuser = BankUser(user=user,iban=iban,creator=creator)
			bankuser.save()

			return HttpResponseRedirect(reverse('bank_users:home')+'?create=1')
		else:
			return HttpResponseRedirect(reverse('bank_users:addUser')+'?create=0')


def readBankingUser(request):
	if request.is_ajax():
		first_name = request.GET.get('first_name')
		last_name = request.GET.get('last_name')
		obj = {'first_name':first_name,'last_name':last_name}
		user = None
		try:
			user = CustomUser.objects.get(first_name__icontains=first_name,last_name__icontains=last_name)
		except:
			return JsonResponse({"failed":"Wrong combination of first name and last name"})
		obj['countrycode']=user.bank_user.iban.countrycode
		obj['checksum']=user.bank_user.iban.checksum
		obj['swiftcode']=user.bank_user.iban.swiftcode
		obj['accountnumber']=user.bank_user.iban.accountnumber
		return JsonResponse(obj)
	else:
		userform = UserForm()
		return render(request,'readUser.html',{'form':userform})

def updateBankingUser(request):
	return render(request,'updateUser.html',{})

def deleteBankingUser(request):
	return render(request,'deleteUser.html',{})