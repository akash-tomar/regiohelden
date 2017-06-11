from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class IBANDetail(models.Model):
	countrycode = models.CharField(max_length=2)
	checksum = models.CharField(max_length=2)
	swiftcode = models.CharField(max_length=4)
	accountnumber = models.CharField(max_length=24)
	def __str__(self):
		return str(self.bank_user.user.first_name+" "+self.bank_user.user.last_name)

class CustomUser(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	class Meta:
		unique_together = ('first_name', 'last_name')
	def __str__(self):
		return str(self.first_name+" "+self.last_name)

class BankUser(models.Model):
	user = models.OneToOneField(CustomUser,related_name="bank_user",blank=True,null=True)
	iban = models.OneToOneField(IBANDetail,related_name="bank_user")
	creator = models.ForeignKey(User,related_name="bank_create_user",blank=True,null=True)
	def __str__(self):
		return str(self.user.first_name+" "+self.user.last_name)
