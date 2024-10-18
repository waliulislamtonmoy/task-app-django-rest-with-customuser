from django.urls import path


#import views
from App_Account.views import UserList,CreateUser
#import rest routers

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', UserList)

urlpatterns = [
    path("signup/",CreateUser.as_view(),name="signup")

]
urlpatterns +=router.urls
