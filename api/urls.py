from django.urls import path
from .import views

urlpatterns = [

    path('task/',views.TaskDetail.as_view()),
    path('task/<int:pk>/',views.Task.as_view()),
]
