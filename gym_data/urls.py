from django.urls import path, include
from .views import (
    TodoListApiView,RegistrationAPI,LoginAPI
)

urlpatterns = [
    path('api', TodoListApiView.as_view()),
    path('register', RegistrationAPI.as_view()),
    path('login', LoginAPI.as_view()),
]