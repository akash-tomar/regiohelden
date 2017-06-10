from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect
import pprint
import json
import urllib2
from djauthapp.models import File
from django.core.files.base import ContentFile
from requests import request
from .models import *
def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'google-oauth2':
        print response["name"]["givenName"]
        print response["name"]["familyName"]
        print response["image"]["url"]
        print response["emails"][0]["value"]
        Images(image=response["image"]["url"])
        obj = {
            "first_name":response["name"]["givenName"],
            "last_name":response["name"]["familyName"],
            "image_id":img_id,
            "email":response["emails"][0]["value"]
        }
        return HttpResponseRedirect('/login?fname='+response["name"]["givenName"])

    if backend.__class__.__name__ == 'FacebookOAuth2':
        url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
        resp = request('GET', url, params={'width': '1000','height':'1000'})
        file = File()
        file.upload.save('{0}_social.jpg'.format("akash"),ContentFile(resp.content))           
        file.save()
        print response
        print response["name"]
        arr=response["name"].split()
        first_name=""
        last_name=""
        if len(arr)>2:
            first_name = arr[0]
            for i in arr[1:]:
                last_name += (i+" ")
        return HttpResponseRedirect('/login?fname='+first_name+'&lname='+last_name)
    elif backend.name=="twitter":
        CONSUMER_KEY = SOCIAL_AUTH_TWITTER_KEY
        CONSUMER_SECRET = SOCIAL_AUTH_TWITTER_SECRET
        ACCESS_KEY = response["access_token"]["oauth_token_secret"]
        ACCESS_SECRET = response["access_token"]["oauth_token"]
        consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
        access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
        client = oauth.Client(consumer, access_token)
        timeline_endpoint = "https://api.twitter.com/1.1/users/show.json?user_id"+str(response["id"])
        response, data = client.request(timeline_endpoint)
        print response
        print data