from django import forms
from .models import *
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = ['first_name','last_name']
	def __init__(self,*args,**kwargs):
		super(UserForm,self).__init__(*args,**kwargs)
		self.fields['first_name'].widget.attrs.update({'placeholder':'First name'})
		self.fields['last_name'].widget.attrs.update({'placeholder':'Last name'})

class IBANForm(forms.ModelForm):
	class Meta:
		model = IBANDetail
		fields = ['countrycode','checksum','swiftcode','accountnumber']
	def __init__(self,*args,**kwargs):
		super(IBANForm,self).__init__(*args,**kwargs)
		self.fields['countrycode'].widget.attrs.update({'placeholder':'Country code','autofocus':'autofocus'})
		self.fields['checksum'].widget.attrs.update({'placeholder':'Check sum'})
		self.fields['swiftcode'].widget.attrs.update({'placeholder':'Swift code'})
		self.fields['accountnumber'].widget.attrs.update({'placeholder':'Account Number'})			# self.fields[field].widget.attrs.update({'class':'form-control'})