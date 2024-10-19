from django.contrib import admin

#import taks model 
from App_Task.models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display=['user','title','date','id']
    ordering=['-id']

admin.site.register(Task,TaskAdmin)
