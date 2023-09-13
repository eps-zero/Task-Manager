from django.contrib import admin
from django.urls import path
from tasks.views import task_list, create_task, delete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_list, name='task_list'),
    path('create/', create_task, name='create_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
]
