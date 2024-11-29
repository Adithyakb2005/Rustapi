from django.shortcuts import render
from django.http import JsonResponse
from . models import *
from . serializer import *
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def sample_fun(req):
    d=Project_use.objects.all()
    s=Sample(d,many=True)
    return JsonResponse(s.data,safe=False)
@csrf_exempt
def model_view(req):
    if req.method=='GET':
        d=Project_use.objects.all()
        s=model_serializer(d,many=True)
        return JsonResponse(s.data,safe=False)
    elif req.method=='POST':
        d=JSONParser().parse(req)
        s=model_serializer(data=d)
        if s.is_valid():
            return JsonResponse(s.data)
        else:
            return JsonResponse(s.errors)