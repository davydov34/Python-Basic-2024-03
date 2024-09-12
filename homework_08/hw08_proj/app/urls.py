from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('list/', views.TaskList.as_view(), name='Task List'),
    path('add/', views.TaskAdd.as_view(), name='Add task'),
    path('details/<slug:pk>/', views.TaskDetailList.as_view(), name='Task Detail'),
]
