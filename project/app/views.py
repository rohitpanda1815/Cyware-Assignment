from django.shortcuts import render
import requests
from .models import User
from datetime import datetime,date
def github(request):
    user = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        user = response.json()
        name=user['name']
        email=user['email']
        if email:
            email=email
        else:
            email='Not Available'
        username=user['login']
        obj=User.objects.filter(username=username)
        if len(obj)==0:
            user1=User.objects.create(username=username,email=email,first_name=name)
            user1.save()
    return render(request, 'display.html', {'user': user})

