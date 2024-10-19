from django.urls import path,include

from App_Task.views import TaskView,TaskDetailView

urlpatterns = [
   path("tasks/",TaskView.as_view()),
   path("tasks/<int:id>",TaskDetailView.as_view()),
]
