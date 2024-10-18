#import models 
from App_Account.models import User,Profile

#import rest_framework Serializer 
from rest_framework.serializers import ModelSerializer


        
class ProfileSerializer(ModelSerializer):
    class Meta:
        model=Profile 
        fields='__all__'
       
       
class UserSerializer(ModelSerializer):
    class Meta:
        model=User 
        fields=['id','email','password']
        depth=1
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user