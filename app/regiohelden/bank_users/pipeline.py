from django.http import HttpResponse
def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'google-oauth2':
        print(response["name"]["givenName"])
        print(response["name"]["familyName"])
        print(response["emails"][0]["value"])
        obj = {
            "first_name":response["name"]["givenName"],
            "last_name":response["name"]["familyName"],
            "email":response["emails"][0]["value"]
        }
        return HttpResponse('Login successful')