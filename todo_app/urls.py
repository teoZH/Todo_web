from django.urls import path
from todo_app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:todo_id>', views.update, name='update_todo'),
    path('delete/<int:todo_id>', views.delete, name='delete_todo')
]