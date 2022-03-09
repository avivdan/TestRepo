from rest_framework.response import Response
from rest_framework.decorators import api_view
from .division import Division
from .util import *
from .inputcheck import isvalidinput
# Create your views here.

@api_view(['POST'])
def AlgoResponseView(request):
    if not isinstance(request.data, dict) or not isvalidinput(request.data):
        return Response(-1)
    prefs = request.data['preferences']
    div = Division(number_of_items=request.data['items'])
    div.add_parties([(i, request.data['mandates'][i]) for i in range(len(prefs))])
    for i in range(len(prefs)):
        div.set_party_preferences(i, prefs[i])
    return Response(str(transpose(bundle_to_matrix(div.divide()))).replace("[","{").replace("]","}"))
    # return Response(transpose(bundle_to_matrix(div.divide())))

