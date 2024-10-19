
#import models
from App_Task.models import Task
from App_Account.models import Profile,User

#import rest_framework
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class UserSerializer(ModelSerializer):
    class Meta:
        model=User 
        fields=['email','password']
        extra_kwargs = {
            'password': {'write_only': True}
        }


        
    
class TaskSerializer(ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'status', 'date']
        depth=1

    def create(self, validated_data):
        return super().create(validated_data)
    
 
            
        