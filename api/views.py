from asyncio.windows_events import NULL
import pyrebase
from django.http import HttpResponse
import os
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .division import Division
from .util import *
from .inputcheck import isvalidinput
from django.core.mail import send_mail
    
# Create your views here.

config = {
    "apiKey": "AIzaSyBrRTqVU9Nk4tMFfKW1aAYs4V3BkmNr8PM",
    "authDomain": "faircoalitiondistribution.firebaseapp.com",
    "projectId": "faircoalitiondistribution",
    "storageBucket": "faircoalitiondistribution.appspot.com",
    "messagingSenderId": "986413816761",
    "appId": "1:986413816761:web:ddcb6c8eda93ff0e46b468",
    "databaseURL": "https://faircoalitiondistribution-default-rtdb.europe-west1.firebasedatabase.app"
}

firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()



#work localy
# def SendMail(request):
#     send_mail(
#             'hello guys',
#            'hey sucker',
#             'avivdandino1@gmail.com',
#             ['aviv.danino@boyar.org.il'],
#             fail_silently=False,
#         )
#     html = "<html><body>email sent.</body></html> " 
#     return HttpResponse(html)

@api_view(['POST'])
def SendMail(request):
    send_mail(
        'hello guys',
        request.data['dec_key'],
        'avivdandino1@gmail.com',
        request.data['email'],
        fail_silently=False,
    ) 
    return Response("email was sent")
        
        
@api_view(['POST'])
def AlgoResponseView(request):
    try:
        if not isinstance(request.data, dict) or not isvalidinput(request.data) or not isinstance(request.data['key'],str):
            return Response(-1)
        database.child(request.data['key'].replace('.','/')).set(str(request.data['preferences']))
        prefs = request.data['preferences']
        div = Division(number_of_items=request.data['items'])
        div.add_parties([(i, request.data['mandates'][i]) for i in range(len(prefs))])
        for i in range(len(prefs)):
            div.set_party_preferences(i, prefs[i])
        return Response(str(transpose(bundle_to_matrix(div.divide()))).replace("[","{").replace("]","}"))
    except:
        return Response(-1)

@api_view(['POST'])
def ReturnSaveView(request):
    try:
        if not isinstance(request.data['key'],str):
            return Response(-1)
        data = database.child(request.data['key'].replace('.','/')).get().val()
        if not isinstance(data,str):
            return Response(-1)
        return Response(database.child(request.data['key'].replace('.','/')).get().val())
    except:
        return Response(-1)