from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class IBANDetail(models.Model):
	countrycode = models.CharField(max_length=2)
	checksum = models.CharField(max_length=2)
	swiftcode = models.CharField(max_length=4)
	accountnumber = models.CharField(max_length=24)
	def __str__(self):
		return str(self.bank_user.user.email)

class BankUser(models.Model):
	user = models.OneToOneField(User,related_name="bank_user")	
	iban = models.OneToOneField(IBANDetail,related_name="bank_user")
	def __str__(self):
		return str(self.user.email)
