from django.urls import path


#import views
from App_Account.views import UserList,CreateUser
#import rest routers

#simpol jwt authentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    
)

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', UserList)

urlpatterns = [
    path("signup/",CreateUser.as_view(),name="signup"),
    path('signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    

]
urlpatterns +=router.urls
