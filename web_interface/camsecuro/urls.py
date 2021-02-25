from django.urls import path
from . import views

urlpatterns = [
    path('', views.place, name='place'),
    path('list/<int:id>', views.index, name='index'),
    path('login/', views.index, name='login'),
]
