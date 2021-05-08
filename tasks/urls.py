from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTask, name='add'),
    path('complete/<task_id>', views.completeTask, name='complete'),
    path('delete/<task_id>', views.deleteTask, name='delete'),
]
