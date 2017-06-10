from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'google-oauth2':
        email = response["emails"][0]["value"]
        user = None
        try:
            user = User.objects.get(email=email)
        except:
            user = User(first_name=response["name"]["givenName"],last_name=response["name"]["familyName"],email = email)
            user.save()
        # import pdb; pdb.set_trace()
        # login(backend.strategy.request, user)
        return HttpResponse('Login successful')