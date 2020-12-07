# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import UserProfile as User
from django.db import IntegrityError
from django.contrib import auth
from django.middleware.csrf import CsrfViewMiddleware
from django.contrib.auth import logout
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import AllowAny
import os
from .serializers import *

from django.conf import settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

abs_path = settings.MEDIA_ROOT+'personal_file/'


@api_view(['POST'])
@permission_classes([AllowAny, ])
def signup(request):
    if request.method=="POST":
        data = json.loads(request.body)
        try:
            saveuser=User.objects.create_user(data.get('username'),password=data.get('password1'))
            os.mkdir(abs_path+str(saveuser.id)+'/')
            os.symlink(abs_path+str(saveuser.id)+'/',abs_path+str(saveuser.id)+'sym')
            saveuser.symlink = abs_path+str(saveuser.id)+'sym'
            saveuser.save()
            return JsonResponse({'Status':"Registration Successful!"})
        except IntegrityError:
            return JsonResponse({'Status':'User Registered Already!'})
    else:
        return render(request,'signup.html',{'form':UserCreationForm})

@api_view(['POST'])
@permission_classes([AllowAny, ])
def login(request):
    if(request.user.is_authenticated):
        return redirect("upload") 
    else:
        if request.method=="POST":
            data = json.loads(request.body)
            username=data.get('username')
            password=data.get('password')
            success=auth.authenticate(request,username=username,password=password)
            if success is None:
                return JsonResponse({"status": False, 'username': username})
            else:
                payload = jwt_payload_handler(success)
                token = jwt_encode_handler(payload)
                auth.login(request,success)
                user=UserSerializer(success)
                user_details = {}
                user_details['name'] = user.data['username']
                user_details['refer_id'] = user.data['refer_id']
                user_details['token'] = token
                return Response(user_details)
        else:
            print("GET request to login")
            return render(request, 'login.html', {'form':AuthenticationForm})

@api_view(['GET'])
def getUser(request):
    print(str(request.user))
    return JsonResponse({'user':str(request.user)})
# Create your views here.
