from django.urls import path
from .import views

urlpatterns = [

    path('task/',views.TaskDetail.as_view()),
    path('task/<int:pk>/',views.TaskView.as_view()),


    path('register/',views.RegisterView.as_view()),
    path('login/',views.LoginView.as_view()),


]
