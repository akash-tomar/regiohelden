from django import forms
from .models import *
from django.contrib.auth.models import User
import re

class UserForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = ['first_name','last_name']

	def __init__(self,*args,**kwargs):
		super(UserForm,self).__init__(*args,**kwargs)
		self.fields['first_name'].widget.attrs.update({'placeholder':'First name'})
		self.fields['last_name'].widget.attrs.update({'placeholder':'Last name'})

	#Raises validation error if string is not alphabet.
	def clean_first_name(self):
		if not re.match(r'^[a-zA-Z]+$', self.cleaned_data.get('first_name')):
			raise TypeError("Only alphabets allowed in names")
		return self.cleaned_data.get('first_name')

	#Raises validation error if string is not alphabet.
	def clean_last_name(self):
		if not re.match(r'^[a-zA-Z]+$', self.cleaned_data.get('last_name')):
			raise TypeError("Only alphabets allowed in names")
		return self.cleaned_data.get('last_name')

class IBANForm(forms.ModelForm):
	class Meta:
		model = IBANDetail
		fields = ['countrycode','checksum','swiftcode','accountnumber']

	def __init__(self,*args,**kwargs):
		super(IBANForm,self).__init__(*args,**kwargs)
		self.fields['countrycode'].widget.attrs.update({'placeholder':'Country code','autofocus':'autofocus'})
		self.fields['checksum'].widget.attrs.update({'placeholder':'Check sum'})
		self.fields['swiftcode'].widget.attrs.update({'placeholder':'Swift code'})
		self.fields['accountnumber'].widget.attrs.update({'placeholder':'Account Number'})
	
	#Raises validation error if string is not alphabet.
	def clean_countrycode(self):
		countrycode = self.cleaned_data.get('countrycode')
		if not countrycode.isalpha() or len(countrycode)!=2:
			raise TypeError("Invalid country code")
		return self.cleaned_data.get('countrycode')

	#Raises validation error if name is not numerical.
	def clean_checksum(self):
		if not self.cleaned_data.get('checksum').isdigit():
			raise TypeError("Checksum can only be numeric")
		return self.cleaned_data.get('checksum')

	#Raises validation error if name is not numerical.
	def clean_accountnumber(self):
		if not self.cleaned_data.get('accountnumber').isdigit():
			raise TypeError("Account number can only be numeric")
		return self.cleaned_data.get('accountnumber')	

	#Raises validation error if name is not alphanumerical.
	def clean_swiftcode(self):
		if not self.cleaned_data.get('swiftcode').isalnum():
			raise TypeError("Swift code can only be alpha numeric")
		return self.cleaned_data.get('swiftcode')

class UpdateForm(forms.Form):
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	countrycode = forms.CharField(max_length=2)
	checksum = forms.CharField(max_length=2)
	swiftcode = forms.CharField(max_length=4)
	accountnumber = forms.CharField(max_length=24)

	def __init__(self,*args,**kwargs):
		super(UpdateForm,self).__init__(*args,**kwargs)
		self.fields['first_name'].widget.attrs.update({'placeholder':'First name','autofocus':'autofocus'})
		self.fields['last_name'].widget.attrs.update({'placeholder':'Last name'})
		self.fields['countrycode'].widget.attrs.update({'placeholder':'Country code'})
		self.fields['checksum'].widget.attrs.update({'placeholder':'Check sum'})
		self.fields['swiftcode'].widget.attrs.update({'placeholder':'Swift code'})
		self.fields['accountnumber'].widget.attrs.update({'placeholder':'Account Number'})

		#Raises validation error if string is not alphabet.
	def clean_first_name(self):
		if not re.match(r'^[a-zA-Z]+$', self.cleaned_data.get('first_name')):
			raise TypeError("Only alphabets allowed in names")
		return self.cleaned_data.get('first_name')

	#Raises validation error if string is not alphabet.
	def clean_last_name(self):
		if not re.match(r'^[a-zA-Z]+$', self.cleaned_data.get('last_name')):
			raise TypeError("Only alphabets allowed in names")
		return self.cleaned_data.get('last_name')

		#Raises validation error if string is not alphabet.
	def clean_countrycode(self):
		countrycode = self.cleaned_data.get('countrycode')
		if not countrycode.isalpha() or len(countrycode)!=2:
			raise TypeError("Invalid country code")
		return self.cleaned_data.get('countrycode')

	#Raises validation error if name is not numerical.
	def clean_checksum(self):
		if not self.cleaned_data.get('checksum').isdigit():
			raise TypeError("Checksum can only be numeric")
		return self.cleaned_data.get('checksum')

	#Raises validation error if name is not numerical.
	def clean_accountnumber(self):
		if not self.cleaned_data.get('accountnumber').isdigit():
			raise TypeError("Account number can only be numeric")
		return self.cleaned_data.get('accountnumber')	

	#Raises validation error if name is not alphanumerical.
	def clean_swiftcode(self):
		if not self.cleaned_data.get('swiftcode').isalnum():
			raise TypeError("Swift code can only be alpha numeric")
		return self.cleaned_data.get('swiftcode')

