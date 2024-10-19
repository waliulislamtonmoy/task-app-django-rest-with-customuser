from django.urls import path


#import views
from App_Account.views import UserList,CreateUser,signin
#import rest routers

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', UserList)

urlpatterns = [
    path("signup/",CreateUser.as_view(),name="signup"),
    path("signin/",signin.as_view())
    

]
urlpatterns +=router.urls
