import pyrebase
import os
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .division import Division
from .util import *
from .inputcheck import isvalidinput
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

@api_view(['POST'])
def AlgoResponseView(request):
    if not isinstance(request.data, dict) or not isvalidinput(request.data) or not isinstance(request.data['date'],str):
        return Response(-1)
    database.child(request.data['date'].replace('.','/')).set(str(request.data['preferences']))
    prefs = request.data['preferences']
    div = Division(number_of_items=request.data['items'])
    div.add_parties([(i, request.data['mandates'][i]) for i in range(len(prefs))])
    for i in range(len(prefs)):
        div.set_party_preferences(i, prefs[i])
    return Response(str(transpose(bundle_to_matrix(div.divide()))).replace("[","{").replace("]","}"))

@api_view(['POST'])
def ReturnSaveView(request):
    if not isinstance(data,str):
        return Response(-1)
    data = database.child(request.data['date'].replace('.','/')).get().val()
    return Response(database.child(request.data['date'].replace('.','/')).get().val())