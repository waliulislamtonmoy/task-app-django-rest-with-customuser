from django.shortcuts import render

#import models
from App_Task.models import Task


#from serializer
from App_Task.serializer import TaskSerializer

#from rest_framework
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class TaskView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def get(self,request):
        try:
            data=Task.objects.all().filter(user=request.user)
            if data is None:
                return Response({'message':'no task found '})
            else:
               serializer=TaskSerializer(data,many=True) 
               return Response({'task':serializer.data})
        except:
            return Response({'status':False,'message':'task not found'})
            

    def post(self, request):
       try: 
            serializer = TaskSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'message': 'New task added successfully', 'Task': serializer.data})
       except Exception as e:    
           return Response({'status': False, 'error': str(e)})
    
class TaskDetailView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def get(self,request,id):
        try:
            data=Task.objects.get(id=id)
            serializer=TaskSerializer(data)
            return Response({'status':True,'task':serializer.data})
        except:
            return Response({'status':True,'message':'task not found'})
        
    
    def put(self,request,id):
        try:
           task=Task.objects.get(id=id)
           if 'title' in request.data:
               task.title=request.data['title']
            
           if 'description' in request.data:
                task.description=request.data['description']
           if 'status' in request.data:
                task.status=request.data['status']
           task.save()
           return Response({'status':True,'message':'successfully updated task'})
        except:
            return Response({'status':False,'message':'Task Not Found or not updated task'})
        
        
       
    def delete(self,request,id):
        try:
            task=Task.objects.get(id=id).delete()
            return Response({'status':True,'message':'task delete successfully'})
        except:
            return Response({'status':False,'message':'task not exist'})
        
        








