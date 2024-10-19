

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("account/",include('App_Account.urls')),
    path("",include("App_Task.urls"))
]
