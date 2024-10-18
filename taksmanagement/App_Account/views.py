from django.shortcuts import render,redirect

#import models
from App_Account.models import User,Profile

#import Serializer 

from App_Account.serializer import UserSerializer

#import rest_framework 
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response


class UserList(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
class CreateUser(APIView):
    def post (self,request):
        data=request.data 
        serializer=UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user':serializer.data})
        return Response({'status':False,'message':serializer.errors})
        
        


