from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='loginUser'),
    path('logout/', views.logoutUser, name='logoutUsers'),
]
