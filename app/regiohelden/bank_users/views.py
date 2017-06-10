from django.shortcuts import render

def home(request):
	# import pdb; pdb.set_trace()
	return render(request,'home.html',{'user':request.user,'request':request})