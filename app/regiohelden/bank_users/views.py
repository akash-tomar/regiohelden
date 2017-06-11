from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.core.urlresolvers import reverse
from bank_users.forms import *
from django.contrib.auth.models import User
from django.http import JsonResponse
import json


#if the user is already logged, redirects to home page.
def login(request):
	if request.user.is_anonymous():
		return render(request,'login.html',{})
	else:
		return HttpResponseRedirect(reverse('bank_users:home'))

#redirects to login page after logging out the user.
def logout(request):
	logout_user(request)
	return HttpResponseRedirect(reverse('bank_users:login'))

#All the operations are listed on this page.
def home(request):
	if request.user.is_anonymous():
		return HttpResponseRedirect(reverse('bank_users:login'))

	'''These variables are flags that keep note of data being created or modified or 
	deleted so that user can be notified accordingly.'''
	created = False
	updated = False
	deleted = False
	# import pdb; pdb.set_trace()
	if 'create' in request.GET:
		created = request.GET.get('create')
		if created=="1":
			created=True
		elif created=="0":
			created=False
	if 'update' in request.GET:
		if request.GET.get('update')=="1":
			updated=True
	if 'delete' in request.GET:
		if request.GET.get('delete')=="1":
			deleted=True
	return render(request,'home.html',{'created':created,'updated':updated,'deleted':deleted })

def createBankingUser(request):
	if request.method=='GET':

		#flag for if the user tried but failed on creation of bank user.
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

		#check the validity of forms
		if userform.is_valid() and ibanform.is_valid():
			first_name = userform.cleaned_data.get('first_name')
			last_name = userform.cleaned_data.get('last_name')

			countrycode = ibanform.cleaned_data.get('countrycode')
			checksum = ibanform.cleaned_data.get('checksum')
			swiftcode = ibanform.cleaned_data.get('swiftcode')
			accountnumber = ibanform.cleaned_data.get('accountnumber')

			user = None
			# import pdb;pdb.set_trace()
			try:
				user = CustomUser(first_name=first_name,last_name=last_name)
				user.save()
			except:
				#User was not found with this combination of first_name and last_name
				return HttpResponseRedirect(reverse('bank_users:addUser')+'?create=0')

			iban = IBANDetail(countrycode=countrycode,checksum=checksum,swiftcode=swiftcode,accountnumber=accountnumber)
			iban.save()
			creator = User.objects.get(pk=request.user.id)
			bankuser = BankUser(user=user,iban=iban,creator=creator)
			bankuser.save()
			return HttpResponseRedirect(reverse('bank_users:home')+'?create=1')
		else:
			#invalid form
			return HttpResponseRedirect(reverse('bank_users:addUser')+'?create=0')

#function to display the details of bank user.
def readBankingUser(request):
	if request.is_ajax():
		first_name = request.GET.get('first_name')
		last_name = request.GET.get('last_name')
		obj = {'first_name':first_name,'last_name':last_name}

		user = None
		try:
			user = CustomUser.objects.get(first_name__icontains=first_name,last_name__icontains=last_name)
		except:
			#user not found with this combination of first and last names.
			return JsonResponse({"failed":"Wrong combination of first name and last name"})

		#get user details and send them to the template.
		obj['countrycode']=user.bank_user.iban.countrycode
		obj['checksum']=user.bank_user.iban.checksum
		obj['swiftcode']=user.bank_user.iban.swiftcode
		obj['accountnumber']=user.bank_user.iban.accountnumber
		return JsonResponse(obj)
	else:
		userform = UserForm()
		return render(request,'readUser.html',{'form':userform})

def updateBankingUser(request):
	if request.method=="POST":

		#In python3 byte cannot be converted to json directly therefore it needs to be decoded.
		body_unicode = request.body.decode('utf-8')
		data = json.loads(body_unicode)

		first_name = data.get('old_first_name')
		last_name = data.get('old_last_name')

		user = None
		try:
			user = CustomUser.objects.get(first_name__icontains=first_name,last_name__icontains=last_name)
		except:
			return JsonResponse({"failed":"Wrong combination of first name and last name"})
		
		#Check whether the creator of the user is trying to modify or not. If not then raise error.		
		if request.user.id != user.bank_user.creator.id:
			return JsonResponse({"failed":"You dont have the permission to update this user."})

		'''this list will keep a track of the fields getting updated so that only those fields need to be saved 
		in the database'''
		updated_fields=[]

		if "first_name" in data:
			user.first_name=data["first_name"]
			updated_fields.append('first_name')
		if "last_name" in data:
			user.last_name=data["last_name"]
			updated_fields.append('last_name')
		user.save(update_fields=updated_fields)

		'''this list will keep a track of the fields getting updated so that only those fields need to be saved 
		in the database'''
		updated_fields=[]
		iban = user.bank_user.iban
		if 'countrycode' in data:
			iban.countrycode=data.get('countrycode')
			updated_fields.append('countrycode')
		if 'checksum' in data:
			iban.checksum = data.get('checksum')
			updated_fields.append('checksum')
		if 'swiftcode' in data:
			iban.swiftcode = data.get('swiftcode')
			updated_fields.append('swiftcode')
		if 'accountnumber' in data:
			iban.accountnumber = data.get('accountnumber')
			updated_fields.append('accountnumber')

		iban.save(update_fields=updated_fields)
		return JsonResponse({"success":True})

	if request.method=="GET":
		#this code will execute when the user has given us the first name and last name and needs other details.
		if "first_name" in request.GET and "last_name" in request.GET:
			first_name = request.GET.get('first_name')
			last_name = request.GET.get('last_name')
			user = None
			try:
				user = CustomUser.objects.get(first_name__icontains=first_name,last_name__icontains=last_name)
			except:
				return HttpResponseRedirect(reverse('bank_users:updateUser')+"?update=0")
			return render(request,'updateUser.html',{'userdetails':user,'iban':user.bank_user.iban})
		
		#This code will execute when user needs to enter the first name and last name to get the record.
		else:
			if "update" in request.GET:
				if request.GET.get("update")=="0":
					userform = UserForm()
					return render(request,'updateUser.html',{'form':userform,'not_updated':True})
			userform = UserForm()
			return render(request,'updateUser.html',{'form':userform})

#Delete the user 
def deleteBankingUser(request):
	if request.method=="POST":
		first_name = request.POST.get("first_name")
		last_name = request.POST.get("last_name")
		user = None
		try:
			user = CustomUser.objects.get(first_name__icontains=first_name,last_name__icontains=last_name)
		except:
			return HttpResponseRedirect(reverse('bank_users:deleteUser')+"?delete=0")
		bankuser = user.bank_user
		iban = bankuser.iban

		user.delete()
		iban.delete()
		bankuser.delete()
		return HttpResponseRedirect(reverse('bank_users:home')+"?delete=1")

	if request.method=="GET":
		if "delete" in request.GET:
			if request.GET.get("delete")=="0":
				userform = UserForm()
				return render(request,'deleteUser.html',{'form':userform,'not_deleted':True})
		userform = UserForm()
		return render(request,'deleteUser.html',{'form':userform})
